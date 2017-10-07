from simplecrypt import decrypt, DecryptionException

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    print(encrypted)
    with open("passwords.txt", "r") as pwd:
        passwords = pwd.read().split("\n")
        for password in passwords:
            print("password = ",password)
            try:
                answer = decrypt(password,encrypted)
            except DecryptionException:
                pass
            else:
                print(answer)
