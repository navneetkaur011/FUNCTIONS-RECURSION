print("---FUNCTIONS---")
# Function is a block of code that performs a specific task.
def diff(a,b):  #Parameters
    d = a-b 
    print(d)
    return d  #These line of code will not return any output.

diff(456,71)  # function call: arguments
diff(98230,6103)

def py():  # function with no parameters 
    print("\nFunctions in Python")

py()

def nothing():   
    print("\nNothing to do.")

print(nothing()) # this will print None
# End of basic function examples.

def square(num):
    return num * num # Note: Always remember to use return statements when you need to store function output.

print(square(4))
print(square(256))

# Function to calculate the average of 3 numbers
def calc_avg(a, b, c):
    sum_val = a + b + c
    avg = sum_val / 3
    print("The average is:", avg)
    return avg

calc_avg(98, 97, 95)


