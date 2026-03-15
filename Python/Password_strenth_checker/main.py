#password strength checker 
password = input("Enter the password: ")

length = len(password) >= 8
upper = any(c.isupper() for c in password)
lower = any(c.islower() for c in password)
digit = any(c.isdigit()for c in password)
special = any(not c.isalnum() for c in password)

total = length + upper + lower +digit + special

if total == 5:
    print(f"{password}  as a password is strong in strength")
elif total == 4:
    print(f"{password} as a password is medium in strength")
elif total == 3:
    print(f"{password} as a password is weak in strength")
else:
    print(f"{password} is not suited")