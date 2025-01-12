#example of float variable
gpa = 3.2
print (f"your gpa is {gpa}")

#example of integer variable
age = 25
print(f"you are {age} years old")

#example of Boolean variable
train = 500
bus = 20
bike = 15

# compare the cost of taking each means of transportation using a conditional statements
# determine the cheapest means of transportation

if train < bus and train < bike:
    cheapest = "train"
elif bus < train and bus < bike:
    cheapest = "bus"
else:
    cheapest = "bike"

print (f'The cheapest means of transportation is {cheapest}')

# use double column in python when your writing a new block of code, when your using a function or key word

# compare the variable above and print the boolean results

print("Is train greater than bus?", train > bus)


#Basic arithmetic in Python
#Addition

friends = 5
friends = friends + 1
print(friends)

friends = 5
friends += 1
print(friends)

#Typecasting
#string, int, float, boolean

name = "bro"
age = 33 
gpa = 3.2
is_student = True

print (type(is_student))



