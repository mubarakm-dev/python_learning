
# Conditional Statement 
#  3 blocks of conditional statements
# if , elif, else
x = 5
if x == 5:
    print(" statement is True ")
elif x < 100:
    print("x is less than 100")
elif x ==5:
    print("x is same as 5")

else:
    print("Wetin be this") 



# Build a ussd application with conditional statement

# Nested Conditional statement
x = 5
y = 20
if x == 5:
    if y < 10:
        print("Bith statement are true")
    else:
        print("only first statemnet is true")
else:
    print("Both statement are false")

#  if the mother if is wrong, nested will not run, it will move to the mother else


name = "Tolu"
age = 40

if age >= 18:
    if age < 80:
        print("You are eligible to vote")
    else:
        print("You are too old")
else:
    print("You are too young to vote")


ussd = input("Enter your USSD: ")
data = 100
if ussd == "*312#":
    print("""
        1. Data Plans
        2. Enjoy 1gb for 4k
        3. Voice plans
        4. Gift Data
    """)
    choice = input("Enter Your choice: ")
    if choice == "1":
        print("""
            1. daily
            2. 2 to 3 days
            3. weekly
            4. 2 weeks
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
         print("You have succesfully subscribed for daily data plan")

        elif choice == "2":
            print("You have successfully subscribed for 3 days data")
        elif choice == "3":
                print("You have successfully subscribed for weekly data")
        elif choice == "2":
                print("You have successfully subscribed for 2 weeks data bundle")
        else:
            print("inavlid choice")
    elif choice == "2":
        print(""" Are you sure you want to subscribe for 1gb for 4k 
            1. Yes
            2. No
        """)
        choice = input("Enter your choice: ")
        if choice =="1":
             print("You have successfully subscribed for 1gb for 4k")
        elif choice == "2":
            print("dial the code again to start again")

        else:
            print("inavlid choice")

    elif choice == "3":
        print("""
            1. $100 for 100 mins
            2. $45 for 10 mins
            3. $90 for 50 mins
            """
        )
        choice = input("Enter your choice: ")

        if choice == "1":
            print("you have successully subscribed for 100 mins for $100")
        elif choice == "2":
            print("you have successully subscribed for 10 mins for $45")
        elif choice == "3":
            print("you have successully subscribed for 50 mins for $50")
        else:
            print("inavlid choice")

    elif choice == "4":
        
        recipientNumber = input("Enter recipient number: ")
        amount = int(input("Enter the amount of data to be shared: "))
        
        if  len(recipientNumber) !=  11:
            print("wrong recipient number")

           
        elif len(recipientNumber) == 11 and amount > 0:
            print(f"you have successfully share {amount}gb of data to {recipientNumber} ")
        else:
            print("amount must be greater that zero")



    else:
        print("Wrong input")

else:
    print("wrong ussd code")



    

    

