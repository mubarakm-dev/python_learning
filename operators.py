# Operators

# Arithmetic Operators
#  1. Addition (+), Subtraction (-), Multiplication (*), Division (/), Modulus (%), Exponentiation (**), Floor Division (//)
# assignment - find the meaning of walrus operator
# x = 5
# y = 10
# print(x + y)  # Addition
# print(x - y)  # Subtraction
# print(x * y)  # Multiplication
# print(x / y)  # Division
# print(x % y)  # Modulus
# print(x ** y)  # Exponentiation
# print(x // y)  # Floor Division

# # comparison Operators
# # 1. Equal to (==), Not equal to (!=), Greater than (>), Less than (<), Greater than or equal to (>=), Less than or equal to (<=)
# x = 6
# y = 7
# print(x > y) # Greater than
# print(x < y) # Less than 
# print(x == y) # Equal to - false
# print(x != y) # Not equal to
# print(x >= y) # Greater than or equal to
# print(x <= y) # Less than or equal to

# score = 50
# if score >= 70 and score <= 100:
#     print("A")

# elif score >= 60 and score <= 69:
#     print("B")
# elif score >= 50 and score <= 59:
#     print("c")

# elif score >= 40 and score <= 49:
#     print("D")
# elif score <= 39:
#     print("You fail the exams")

# else:
#     print("Invalid score")


# score = input("Enter your score: ")
# score = int(score)  # Convert the input to an integer
# if score in range(70, 100):
#     print("A")

# elif score in range(60, 69):
#     print("B")

# elif score in range(50, 59):
#     print("C")

# elif score in range(45, 49):
#     print("D")

# elif score in range(40, 44):
#     print("E")

# elif score in range(0, 39):
#     print("You fail the exams")
# else:
#     print("Invalid score")





# Logica;l Operators
# 1. AND (&), OR (|), XOR (^), NOT (~), Left Shift (<<), Right Shift (>>)

# x = 6
# y = 200

# if x >= 5 and y <= 130:
#     print("Valid")
# else: 
#     print("Invalid")

# if x > 10 or y < 20:
#     print("Valid")

# else: 
#     print("Invalid")


# # Logical not
# if not (x >= 5 and y <= 130):
#     print("Valid")
# else: 
#     print("Invalid") # 



# membership Operator : 
# in, not, in

berries = ["strawberry", "blueberry", "raspberry", "blackberry"]
if "blackberry" in berries:
    print("Yes, blackberry is in the list")

else:
    print("No, blackberry is not in the list")

#  we can use membership operators in any of the sequnce data type, list and tupple


# Assignment operator
# -= , +=, *=, /=, %=, **=, //=, :=, >>=, <<=

x = 5
# x += 10
# print(x)

# x -= 10
# print(x)

# x *= 2
# print(x)

# x /= 2
# print(x)

# x %= 2
# print(x)

# x **= 3
# print(x)


# Identity Operator
# is, is not
#  is is 
x = 100
y = 100

print(x is y) # True
print(x is not y) # False

a = [100, 200, 300, 400]
b = [100, 200, 300, 400]

print(a is b) # False - because they are different objects in memory
print(a is not b) # True

# Bitwise Operators
# 1. AND (&), OR (|), XOR (^), NOT (~), Left Shift (<<), Right Shift (>>)

# xor - only one must be true
# or - at least one must be treu

print(90 & 7) # answer is 2
print (90 | 7)
print(90 ^ 7)

x = 90 & 7
# for negation: check binary eq of 90, and 7 and AND the both, then negate the answers of the AND &




