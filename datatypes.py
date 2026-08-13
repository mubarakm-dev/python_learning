# Tupple

names = ("kenny", "laide", "kola", "ola", "bola", "jola")
# tupples can be indexed
# tupples are not mutable, which means item in tupple can not be chnaged
# tupples is ordered

print(names)
print(type(names))


print(names[0])
print(names[0:5])


# disctionaries
# properties:
# dictionaris are represneted in keys and values
# you can not slice

user = {
    "name": "kenny",
    "age": 20,
    "course": "DSA",
    "gender": "male",
    "address": {
        "street": "123 Main St",
        "city": "Lagos",
        "state": "Lagos State"
    }

}

print(user)
print(type(user))

print(user["age"])
print( user["name"], user["course"])    # to print 2 values in the dictionary
user["age"] = 10
print(user)

print(user["address"]["city"])  # to print the city in the address dictionary



# Range - 

x = range(0, 100)
y = list(x) #
print(x)  # this will print the range object
print(y) # this will print the range in a list format
print(type(y)) # this will print the type of the list object, which is list      
print(type(x)) # this will print the type of the range object, which is range, we can not print the range object directly, we need to cast it in order to print from 0

#  we need to cast it in order to print from 0
# range collect 3 parameters, start, stop and step, step is optional, if not provided it will default to 1

y = range(0, 100, 5)
print(list(y))  # to print the range in a list format with step of 5


#  sets
#  collection of unique elements,
#  sets are unordered and unindexed, 
# sets are mutable but the elements in the set must be immutable


banks = {"GTB", "UBA", "Access Bank", "Zenith Bank", "First Bank", "GTB"}
print(type(banks))


# python precendence




