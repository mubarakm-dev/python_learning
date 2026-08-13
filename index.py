print("Welcome to Python class")





# four modules
# module 1: 
# Indentation
# commenting
# data types
# python operators
# conditional statements
# Python collections and arrays
 

#  indentation
# x = 5
# y = 10
# if x > y:
#     print("x is greater than y")
# else:
#     print("x is not greater than y")

# commenting
# multi level commenting

# """
# This is a Registration page
# """
# print("Thank you")

# Python Variables
# variables are like containers where we keep our data types in python 
# x = 5 // x is the variable

# Rules of variable declarations
# 1. All variables must start with underscores or characters
# var = 5
# _var = 5
# 999var = 5 this is wrong

# 2. variable are case sensitive
# age = 5
# Age = 10

# 3. variables can not includes space in btw
# 4. variables must not includes python keywords



# types of 
# # mutltiple var to multiple values declaration
# x,y = 5, 6 // 5 is assigned to x and 6 is assigned to y, called tuple unpacking
# print(type(x))
# print(type(y))

# # multiple var to a single value declaration
# x = y = z = 60
# print(x)
# print(y)


# first_fruits, *second_fruit, last_fruit = ["orange", 'apple', 'mango', 'strawberry' 'banana']
# # if you add an asterisk * to a variable it means remaining, and the last fruit will take the last index whihc is [-1] 

# #  different casing in python
# # -  camelCase
# myVariableName = 5
# print(myVariableName)
# # - snake_case
# my_variable_name = 5
# print(my_variable_name)

# #  - PascalCase
# MyVariableName = 5
# print(MyVariableName)
# #
# # - kebab-case
# # my-variable-name = 5 this is wrong

# # SCREAMING_SNAKE_CASE
# MY_VARIABLE_NAME = 5
# print(MY_VARIABLE_NAME)



# PYTHON INPUT
# PYTHON OUTPUT
# cocatination
# CASTING


# name = input("What is your name:")
# print("My name is", name)

# x = int(input("enter your first number:")) 
# y = float(input("enter your second number")) 
# print(x+y)


# x = str(5)
# print(type(x))


# concatenation is the method of adding varables to a collection ofstrings values
# - using the addition operator
# - using formating strings
# - concatinate using the .join function - assignement

# name = input("Enter your name: ")
# age = int(input("Enter your age"))
# year_of_birth = 2026 - age
# print("My name is" + " " + name + " " "and I am" + " " + age + " " + "years old")

# print(f"My name is {name} and I am {age} years old")

# print(f"My name is {name}, and I am {age} years old, I was born in {year_of_birth} ")

# create a regsitration form and recieve the inputs of the users then print out the recieve generating account number for the user

# import random as rd
# account_number = rd.randint(1000000000, 9999999999)
# print(account_number)


# Introduction to data Types

#  1. Text Type
#  - strings

# 2. Number data types
# - int, float, complex

# 3. Boolean data types
#  - true, false

# 4. Sequence data types
#  - list, tuples, range

# 5. Mapping data types
#  - dictionary, sets

# 6. Binary data types
#  - bytes, bytearray, memoryview

#  none data types

# strings
gender = "female"

print(gender.capitalize)


# int and float
x = 4
y = 4.0


# complex 
# x = 4 + 5j
# print(type(x))

# float
x = 44E5
print(type(x))

cars = ['benz', 'camry', 'bmw', "lambo", "porche", "keke"] # list
# properties of list
# list is mutable
#list can be indexed 
# list are ordered

# print(type(cars))

# cars[0] = "toyota"
# print(cars)

# print(cars[0:3]) # this will print the first three items in the list - slice
# print(cars[2:]) # this will print the third item to the last item in the list

# print(cars[-1]) # this will print the last item in the list
# print(cars[-3: - 1])  # this will print the third to the second item from the end which are lambo and porche

# print(len(cars)) # this will print the length of the list




