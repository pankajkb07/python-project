# a-z   pankajkumarbais7067@gmail.com
# A-Z
# 0-9
# . _ time 1
# @ time 1
# . 2,3
import re
email_conditinon="^[a-z A-Z]+[\._]?[a-z A-Z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your Email : ")

if re .search(email_conditinon,user_email):
    print("Right Email")
else:
    print("Wrong Email")