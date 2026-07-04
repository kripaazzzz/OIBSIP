import random
import string

charValue = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

pass_len = int(input("Enter password length: "))
password = ""
for i in range(pass_len):
    password = password + random.choice(charValue)

print("Password: ", password)
