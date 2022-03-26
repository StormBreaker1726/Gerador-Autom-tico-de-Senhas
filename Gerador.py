import random
import string
import os
from random import sample

def shuffle(stri):
    a = sample(stri,len(stri))
    d = ''.join(a)
    return d


def password_generation(cont, qty_of_characters):
    i = 0

    password = ""

    while i < qty_of_characters:
        if random.randint(0, 2) == 0:
            password += str(random.choice(string.ascii_letters))
        if random.randint(0, 2) == 1:
            password += str(random.randint(0, 9))
        if random.randint(0, 2) == 2:
            password += str(random.choice(['#', '$', '&', '!', '*', 'ß', '@']))
        i = i + 1
    
    pas = shuffle(password)
    
    passwords_file = open("passwords.txt", "a") #open file
    
    passwords_file.write("Password number " + str(cont) + ": " + str(pas))
    
    passwords_file.write("\n \n")
    
    passwords_file.close()



qty_to_be_generated = int(input("How many passwords must be generated?  "))#get how many passwords to generate
qty_of_characters = int(input("How many characters in the passwords?  "))

cont = 0;  

while cont < qty_to_be_generated:
    password_generation(cont, qty_of_characters)
    cont += 1