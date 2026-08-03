print("---FUNCTIONS---")
# Function is a block of code that performs a specific task.
def diff(a,b):  #Parameters
    d = a-b 
    print(d)
    return d  #These line of code will not return any output.
print("--Difference using functions-- ")
diff(456,71)  # function call: arguments
diff(98230,6103)

print("\n--Function with no parameters--")
def py():  # function with no parameters 
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
    print("The average is:", avg)
    return avg
calc_avg(98, 97, 95)

 
# Demonstrating built-in functions vs user-defined functions

# Built-in functions example
print("\nLength of string:", len("ApnaCollege"))
print("Type example:", type(10))

# Default arguments example taught in Apna College
def cal_prod(a=1, b=2):
    print("Product is:", a * b)
    return a * b

cal_prod()  # Uses default values
cal_prod(5) # Uses a=5, b=2

# Function to print elements of a list in a single line

cities = ["Delhi", "Gurgaon", "Noida", "Mumbai", "Pune"]
heroes = ["thor", "ironman", "captain america", "batman"]

def print_len(list_item):
    print("Total items:", len(list_item))
    for item in list_item:
        print(item, end=" ")
    print() # New line

print_len(cities)
print_len(heroes)
