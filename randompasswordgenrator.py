#random password generator code by Pankaj Kumar Bais

import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_"

while True:
    pass_length = int(input("Enter the length of require password: "))
    pass_count = int(input("Enter the number of require passwords: "))
    
    for i in range (0,pass_count):
        password = ""
        for j in range (0,pass_length):
            pass_char = random.choice(characters)
            password = password+pass_char
        print ("The generated password is",password)
    print("Done")
    repeat = input("Do you want to generate more passwords ? ")
    if repeat=="no" or repeat == "No" or repeat=="NO":
        print("Ok")
        break
    
print("Be Secure,Thank You")
