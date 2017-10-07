#from simplecrypt import decrypt, DecryptionException
#import simplecrypt
from simplecrypt import *

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    print(encrypted)
    with open("passwords.txt", "r") as pwd:
        passwords = pwd.read().split("\n")
        #passwords = pwd.readlines()
        for password in passwords:
            #password.pop()
            print("password = ",password)
            try:
                answer = decrypt(password,encrypted)
            except DecryptionException:
                pass
            else:
                print(answer)
