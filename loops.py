
# Loops
# break and continue


# expression, iteration and iterable

# iterate = i, a variable that is meant to keep the value inside the interable
# iterable - data types where you have your value from  (mostly in mapping or sequence data types )
# expression - what we want to perform
# iteration - the act of looping
#

# break - stop 

fruits = ["berries", "orange", "banana", "melon", "cherry"]

for i in fruits:
    print(i)
    if i == "melon":
        break
    print("close end")



# nested for loop
# for i in range(1, 13):
#     print (f"Multiplication table {i}")
#     for x in range(1, 13):
#         print(f"{i} * {x} = {i * x}")


# read on while loop

x = 1
while x >= 1:
    if x == 5:
        break
    print(x)
    x += 1

y = 1

while x <= 10:
    print(x)
    x += 1

colors = ["blue", "orange", "white", "green", "indigo"]

for i in colors:
    print(i)
    if i == "green":
        break

i = 0
while i < len(colors):
    x = colors[i]
    print(x)
    if x == "green":
        break
    i += 1


i = 1
while i < 10:
    if i == 3:
        break
    print(i)
    i += 1


# Ticket system

# tickets = 10
# vip_ticket = 3
# while tickets <= 10:
#     name = input("Enter your name: ")
#     age = int(input("Enter your Age: "))

#     if age < 18:
#         print("You are too young for this, go and watch anime")
#         break
       
#     print("Ticket available")
  
#     print("""
#         1. Regular
#         2. VIP
#     """)
    
#     option = input("which ticket do you want: ")
#     if option == "1":
#         print("""
#         Welcome to the Home of Fortune
#         choose the film to watch below
#         1. Annie
#         2. Ninja
#         3. Spiderman
#         """)
#         choice = input("Enter your choice")
       
#         if choice == "1":
#             tickets -= 1
#             print(f" Congrats, ticket purchased successfully,  selling out soon, {tickets} tickets remaining, you can purchase for your loved ones ")
#             print("Go to room 4, for a regular")

#         elif choice == "2":
#             tickets -= 1
#             print(f" Congrats, ticket purchased successfully,  selling out soon, {tickets} tickets remaining, you can purchase for your loved ones ")
#             print("go to room 309, for a regular")

#         elif choice == "3":
#             tickets -= 1
#             print(f" Congrats, ticket purchased successfully,  selling out soon, {tickets} tickets remaining, you can purchase for your loved ones ")
#             print("go to room 306, for a regular")
#         else:
#             print("Invalid Selection")

#     elif option == "2":
#         if vip_ticket < 1:
#             print("No more ticket")
#             continue

#         print("""
#                 Welcome to the Home of Fortune
#                 choose the film to watch below
#                 1. Annie
#                 2. Ninja
#                 3. Spiderman
#         """)
#         choice = input("Enter your choice")
               
#         if choice == "1":
#             vip_ticket -= 1
#             print(f" Congrats, ticket purchased successfully,  selling out soon, {tickets} tickets remaining, you can purchase for your loved ones ")
#             print("Go to room 4, for a regular")
        
#         elif choice == "2":
#             vip_ticket -= 1
#             print(f" Congrats, ticket purchased successfully,  selling out soon, {tickets} tickets remaining, you can purchase for your loved ones ")
#             print("go to room 309, for a regular")
        
#         elif choice == "3":
#             vip_ticket -= 1
#             print(f" Congrats, ticket purchased successfully,  selling out soon, {tickets} tickets remaining, you can purchase for your loved ones ")
#             print("go to room 306, for a regular")
#         else:
#             print("Invalid Selection")
# else:
#     print("No more ticket")

    

# i = 0
# while i > 0:
#     print(i)
#     i += 1


# range returns integer 

# for x in range(1, 13):
#     print(f"Multiplication Table {x}")
#     for y in range(1, 13):
#         print(f"{x}*{y} = {x * y} ")
#         continue

