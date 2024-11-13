name = "Damian"
last_name = "Savage"
cohort = 52
is_active = True

print(name + " " + last_name + " #" + str (cohort))

integer = 10 # Integer
float_num = 3.14 # Float
text = "Hello" # String
is_sunny = False # Boolean

# ====== Type Conversion ========
num = 9.75
print(int(num)) # Convert a Float to an integer

age = 25
print(int(age)) # convert an integer into a string

price = "19.99"
print(float(price)) # convert a string to float

# Challenge 
# Create some variables called: name, last_name, age and show them in a print
# "Hello, name last_name, you are age years old."
name = "Tigger"
last_name = "Savage"
age = 5

print("Hello " + name + " " + last_name + ", you are " + str(age) + " years old." ) 
# print(f"Hello, {name} {last_name}, you are {str(age)} years old.") easier method

# ==== Operators ====

x = 5
y = 3

print(x + y) # Addition
print(x - y) # Subtraction  
print( x * y) # Multiplication
print(x / y) # Division
print(x % y) # Modulus
print(x ** y) # Exponentation

# ==== Comparison Operators ====

a = 10
b = 5

print(a == b) # Equal to 
print(a != b) # Not equal to 
print(a > b) # Greater than
print(a < b) # Less than
print(a >= b) # Greater than or equal to 
print(a <= b) # Less than or equal to

x = 5
y = 10
print("....")
print(x > 3 and y < 15) # True, because both conditions are met
print(x > 3 or y > 15)  #True, because X is greater than 3
print(not (x > 3)) # False, 

# ==== Lists ====
fruits = ["apple", "banana", "cherry", "watermelon"]
print(fruits[0])
print(fruits[-1]) # Last minus however many

# List Methods

fruits.append("grape") # Adds to a list
fruits.remove("banana") # Removes from list

print(fruits.pop(1)) # Removes and prints at index 1

print(fruits.index("grape")) # returns index of grape 
# ==== If Statements ====

age = 20

if age >= 18:
    print("You are an adult")
else:
    print ("You are a minor")
if x > 10:
    print("X is greater than 10")
elif x == 10:
    print("X is equal to 10")
else:
    print("X is less than 10")

# ==== For Loops ====

for i in range(5):
    print (i)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
# === Functions ====

def greet():
    print("Hello from greet function")

greet()

def say_hi(name):
    print(f"Hi {name}")
    
say_hi("Damian")


def comment_division():
    print("===========")

# ==== Variables ====
