import os


def check_status(code):
  if code==200:
    print("Success")
  else:
    print("Error",code)

'''
A linter is like an automatic code reviewer.

It scans your code without running it, flags issues, and
enforces a consistent style so your project looks like it
was written by a professional team.

Create a virtual environment:
python3 -m venv venv

Activate the virtual environment:
source ./venv/bin/activate

Install the latest version of the Flake8 linter
in the virtual environment:
pip install flake8

Run the linter:
flake8 example.py
'''