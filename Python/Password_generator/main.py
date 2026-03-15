#random password generator
import random 

characters = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*/.,:'
num = int(input("Enter the number of digits : "))

password = ""
for i in range(num):
    password += random.choice(characters)

print("password :", password)
