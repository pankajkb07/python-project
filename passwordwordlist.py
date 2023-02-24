#python password list for brute force attack code by pankaj kumar bais

from itertools import product
from string import*

value = ascii_letters + digits + punctuation

for i in range(1,2):
    for j in product(value,repeat = i):
        word = "".join(j)
        p = open("password.txt","a")
        p.write(word)
        p.write("\n")
