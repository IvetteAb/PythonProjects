# mini project - random password generator

# import the relevant modules
from random import randint

# create an all uppercase password,
# start w/ an empty string --> L11
# to figure out how long you want the password to be, for loop --> L12
# random integer between 65 & 90, which corresponds to a letter in the alphabet --> L13
# take the original password, make it equal to a string then add i (random letter) --> 14
# it'll repeat 12 times & add a random letter each time
# password = the string of the pw (which began as an empty string, L14) + uppercase (i) on loop * 10
# to make it lowercase --> i = chr(randint(65, 90)).lower()
password = ""
for i in range(12):
    i = chr(randint(65, 90))
    password = str(password) + i
print(password)

# upper & lower case alternating password --> 10 letters long, random letters
# uppercase characters --> L25/26 & lowercase characters --> L27/28
# ij loop * 5
# pw = string of the pw (which began as an empty string, L23) + uppercase (i) & then + lowercase (j) loop, L29
password2 = ""
for i in range(5):
    i = chr(randint(65, 90))
    for j in range(5):
        j = chr(randint(65, 90)).lower()
    password2 = str(password2) + i + j
print(password2)

# all lowercase password
# password = the string of the pw (which began as an empty string, L34) + uppercase (i) on loop * 16
password = ""
for i in range(16):
    i = chr(randint(65, 90)).lower()
    password = str(password) + i
print(password)
