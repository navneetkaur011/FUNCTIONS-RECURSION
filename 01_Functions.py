print("---FUNCTIONS---")
# Function is a block of code that performs a specific task.
def diff(a,b):  #Parameters
    d = a-b 
    print("The difference of", a, "and", b, "is:", d)
    return d  #These line of code will not return any output.
print("--Difference using functions-- ")
diff(456,71)  # function call: arguments
diff(98230,6103)

print("\n--Function with no parameters--")
def py():
    print("Functions in Python")
py()

print("\n--None function--")
def nothing():   
    print("Nothing to do.")
print(nothing()) # this will print None
# End of basic function examples.

print("\n--Function to calculate the square of a number--")
def square(num):
    return num * num # Note: Always remember to use return statements when you need to store function output.
print(square(4))
print(square(256))

print("\n--Function to calculate the average--")
# Function to calculate the average of 3 numbers
def calc_avg(a, b, c):
    sum_val = a + b + c
    avg = sum_val / 3
    print("The average of", a,",", b, "and", c, "is:", avg)
    return avg
calc_avg(98, 97, 95)

print("\n--Built-in functions--") 
# Demonstrating built-in functions vs user-defined functions
print("Length of string:", len("Built-in Functions"))
print("Type:", type(10))

print("\n--Default Parameters--")
#Assigning a default value to parameter, which is used when no argument is passed.
def product(a=18, b=2):
    print("Product of", a, "and", b, "is:", a * b)
    return a * b
product()  # Uses default values
product(5) # Uses a=5, b=2
