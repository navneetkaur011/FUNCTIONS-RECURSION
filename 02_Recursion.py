# Recursion is when a function calls itself repeatedly to solve a smaller sub-problem until it reaches a base case.

# Recursive function to calculate the sum of first n natural numbers
def calc_sum(n):
    # Base case: stopping condition
    if n == 0:
        return 0
    return n + calc_sum(n - 1)

sum_result = calc_sum(5)
print("The sum of first 5 natural numbers is:",sum_result)

# Recursive function to calculate factorial
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("The factorial of 4 is:",factorial(4))

# Recursive function to find the power of a number (stack power: x^n)
def calc_power(base, n):
    # Base case
    if n == 0:
        return 1
    # Recursive step
    return base * calc_power(base, n - 1)

print("2 to the power 3 is:", calc_power(2, 3))
