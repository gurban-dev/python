import requests

class AciSession:
  def __init__(self, apic_url, username, password):
    self.apic_url = apic_url
    self.username = username
    self.password = password
    self.cookies = None

  def login(self):
    login_url = f"{self.apic_url}/api/aaaLogin.json"
    payload = {"aaaUser": {"attributes": {"name": self.username, "pwd": self.password}}}
    response = requests.post(login_url, json=payload, verify=False)
    response.raise_for_status()
    token = response.json()['imdata'][0]['aaaLogin']['attributes']['token']
    self.cookies = {'APIC-cookie': token}
    print("[+] Logged in successfully.")

  def get_tenants(self):
    tenants_url = f"{self.apic_url}/api/node/class/fvTenant.json"
    response = requests.get(tenants_url, cookies=self.cookies, verify=False)
    response.raise_for_status()
    tenants = response.json()['imdata']

    for t in tenants:
      print("-", t['fvTenant']['attributes']['name'])

if __name__ == "__main__":
  requests.packages.urllib3.disable_warnings()
  session = AciSession("https://sandboxapicdc.cisco.com", "admin", "ciscopsdt")
  session.login()
  session.get_tenants()