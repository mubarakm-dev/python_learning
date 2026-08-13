import random as rd

name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
account_number = rd.randint(1000000000, 9999999999)
gender = input("Enter your gender: ")
print(f"Registration successful! Welcome {name}. Your account number is {account_number}.")


letters = ["P", "y", "t", "h", "o", "n"]
result = "".join(letters)
print(result)  