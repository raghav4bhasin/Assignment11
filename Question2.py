import re

chk_num = input("Enter a valid Phone Number (Eg. +91-0123456789): ")

m = re.search('^[+][9][1][-][6-9][\d]{9}', chk_num)

if m != None:
    print("This was a Valid Phone Number.")
else:
    print("ERROR!! This was an Invalid Phone Number.")
