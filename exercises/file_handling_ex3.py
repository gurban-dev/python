'''
Scenario: Website Access Logs Analysis

Your website keeps an access log in a file called access.log.
Each line records the timestamp, user ID, and the page they visited:
2025-10-01 12:01:01,user123,/home
2025-10-01 12:03:15,user456,/about
2025-10-01 12:04:30,user123,/products
2025-10-02 09:15:10,user789,/home
2025-10-02 10:22:05,user123,/home


Task:
Read the access.log file.

Compute the following:
The total number of unique users.

The total number of page visits per page.

The most active user (the user with the most page visits).


Print a summary like:
Unique users: 3
Page visits:
   /home: 3
   /about: 1
   /products: 1
Most active user: user123


Hints:
Use with open(filename, 'r') as f to read the file.

Use the .split(',') method to separate timestamp, user ID, and page.

A set is useful for tracking unique users.

A dictionary can help count page visits and user activity.

You may need to iterate through the file once while updating all counts.
'''