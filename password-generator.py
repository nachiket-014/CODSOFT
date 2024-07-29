# python programming internship in codsoft 
# task 3 -- Password Generator


import random
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'

length = int(input("Enter the desired length of the password: "))
password = ''

for i in range(length):
    password += random.choice(characters)
# output the password 
print(f"Generated Password: {password}")
