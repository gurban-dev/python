'''
Scenario:
You work for a small web service, and your server
generates a log file called server.log. Each line
contains the timestamp and the status of a request:

2025-10-01 12:01:01 - SUCCESS
2025-10-01 12:03:15 - FAIL
2025-10-01 12:04:30 - SUCCESS

Task:
1. Read the log file.

2. Count how many requests were successful and how many failed.

3. Print a summary like:
   SUCCESS: 10
   FAIL: 3

Hints:
Use with open(filename, 'r') as f for reading files.

The .split() method can help extract the status from each line.

A dictionary can be useful for counting statuses.
'''