print("Ques.1- Write a program to print the length of a list.")

cities = ["Delhi", "Gurgaon", "Noida", "Mumbai", "Pune"]
heroes = ["thor", "ironman", "captain america", "batman"]

def print_len(list_item):
    print("Total items:", len(list_item))
    for item in list_item:
        print(item, end=" ")
    print()

print_len(cities)
print_len(heroes)

print("\nQues.2- Find the factorial of n using a loop inside a function.")

def cal_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("The factorial of", n, "is:", fact)
    return fact

cal_factorial(5)
cal_factorial(4)