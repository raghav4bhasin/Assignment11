import re

email = input("Email: ")

m = re.search('^[a-zA-Z][a-zA-Z0-9]*[@](gmail.com|yahoo.com|outlook.com)', email)

if m != None:
    print('Email Verified!')
else:
    print('Invalid Email Address!')
