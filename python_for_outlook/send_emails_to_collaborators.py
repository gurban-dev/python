import os
import httpx
from dotenv import load_dotenv
from ms_graph import get_access_token
import requests
from office365.sharepoint.client_context import ClientContext
import requests

# Step 1: Install the necessary library:
# pip install office365-rest-python-client

'''
connect_to_sharepoint() accepts three parameters:
sharepoint_url: The URL of the SharePoint site you want to
                connect to.

username: The username to use for authentication.

password: The password associated with the username.
'''

# Step 2: Connect to SharePoint
def connect_to_sharepoint(sharepoint_url, username, password):
  '''
  The next line creates a ClientContext object, which is the
  main entry point for interacting with SharePoint using the
  Office365-REST-Python-Client library.

  The method .with_user_credentials(username, password) sets
  the credentials for the ClientContext and uses them to
  authenticate the connection.'''
  ctx = ClientContext(sharepoint_url).with_user_credentials(username, password)

  '''
  Send the authenticated ClientContext object, which can then
  be used to perform operations on the SharePoint site, back
  to where this function was invoked.'''
  return ctx

'''
get_collaborators() accepts three parameters:
ctx: A ClientContext object, which is used to interact with
     SharePoint. This object should be authenticated and
     connected to the SharePoint site.

list_name: The title of the SharePoint list from which to
           retrieve data.

project_name: The name of the project for which collaborators
              are to be retrieved.
'''

# Step 4: Retrieve collaborators from SharePoint
def get_collaborators(ctx, list_name, project_name):
  '''
  Retrieve a SharePoint list object by its title using
  the get_by_title() method of the lists property of the
  web object within the ClientContext.

  Properties of the ClientContext class:
  https://learn.microsoft.com/en-us/previous-versions/office/sharepoint-csom/ee543738(v=office.15)#properties

  ListCollection.GetByTitle method:
  https://learn.microsoft.com/en-us/previous-versions/office/sharepoint-csom/ee545815(v=office.15)
  '''
  list_obj = ctx.web.lists.get_by_title(list_name)

  '''
  list_obj.items: This accesses the items within the SharePoint list.

  .filter(f"Project eq '{project_name}'"):
  This applies a filter to retrieve only items where the Project
  field matches the specified project_name. The f-string formatting
  is used to insert the project_name into the filter string.

  .get(): This method is used to prepare the query for execution.

  .execute_query(): This executes the query and retrieves the filtered
  items from SharePoint. The result is stored in the items variable.
  '''
  items = list_obj.items.filter(f"Project eq '{project_name}'").get().execute_query()

  # An empty list for storing the collaborators
  # retrieved from SharePoint.
  collaborators = []

  for item in items:
    '''
    Iterates over each item in the filtered list.

    For each item, extract the value of the Collaborators field
    (or whatever field name is specified) and appends it to the
    collaborators list.
    
    You may need to replace 'Collaborators' with the actual field
    name in your SharePoint list if it differs.

    The name of the field, such as 'Collaborators', is determined
    by the internal name of the field in SharePoint.

    Perhaps the name 'Collaborators' can be seen in the SharePoint
    list settings for this particular SharePoint list.

    ListItem properties:
    https://learn.microsoft.com/en-us/previous-versions/office/sharepoint-csom/ee546698(v=office.15)#properties
    '''
    collaborators.append(item.properties['Collaborators'])

  return collaborators

def get_collaborators(ctx, list_name, project_name):
  list_obj = ctx.web.lists.get_by_title(list_name)
  items = list_obj.items.filter(f"Project eq '{project_name}'").get().execute_query()

  collaborators = []
  for item in items:
    # Assuming 'Collaborators' is a field containing emails
    collaborators.append(item.properties['Collaborators'])

  return collaborators

'''
send_emails() accepts two parameters:
access_token: A string representing the access token
obtained from Microsoft Graph, which is needed to
authenticate the request.

collaborators: A list of strings, where each string is
an email address of a project collaborator.
'''

# Step 6: Send emails to collaborators
def send_emails(access_token, collaborators):
  '''
  Assign the Microsoft Graph API endpoint for sending an
  email.

  The endpoint is actually: /me/sendMail endpoint. Using
  /me implies that the email will be sent on behalf of
  the user whose account is associated with the access
  token.'''
  graph_url = "https://graph.microsoft.com/v1.0/me/sendMail"

  '''
  The Authorization: Bearer {access_token} header validates the
  request by proving the app has permission to access emails in
  Outlook.'''
  headers = {
    'Authorization': 'Bearer ' + access_token
  }

  for email in collaborators:
    message = {
      "message": {
        "subject": "Important Update for Your Project",
        "body": {
          "contentType": "Text",
          "content": "Hello,\n\nThis is an important update regarding your project."
        },
        "toRecipients": [{"emailAddress": {"address": email}}]
      }
    }

    response = requests.post(graph_url, json=message, headers=headers)

    # The 202 status code indicates that the server has received
    # and understood a client's request. The server may still be
    # processing it.
    if response.status_code == 202:
      # "text" is an attribute of the httpx.Response class
      # that holds the response body as a string.
      raise Exception(f'Failed to send email: {response.text}')
    print('Email sent successfully.')

def main():
  sharepoint_url = input("Enter your SharePoint site URL: ")
  username = input("Enter your SharePoint username: ")
  password = input("Enter your SharePoint password: ")

  # A SharePoint list is a tool used in Microsoft SharePoint
  # to organise and manage data within an organisation.
  list_name = input("Enter the name of the SharePoint list: ")

  ctx = connect_to_sharepoint(sharepoint_url, username, password)

  # Step 3: Prompt user for project name
  project_name = input("Enter the name of the SharePoint project: ")

  collaborators = get_collaborators(ctx, list_name, project_name)

  load_dotenv()
  
  APPLICATION_ID = os.getenv('APPLICATION_ID')

  CLIENT_SECRET = os.getenv('CLIENT_SECRET')

  SCOPES = ['User.Read', 'Mail.ReadWrite']

  try:
    # Step 5: Authenticate with Microsoft Graph API
    access_token = get_access_token(
      application_id=APPLICATION_ID,
      client_secret=CLIENT_SECRET,
      scopes=SCOPES
    )

    send_emails(access_token, collaborators)
  except httpx.HTTPStatusError as err:
    print(f'HTTP Error: {err}')
  except Exception as err:
    print(f'Error: {err}')

main()