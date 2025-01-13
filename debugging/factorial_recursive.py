#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    This function calculates the factorial of a given number n using recursion.

    Parameters:
    n (int): The number for which the factorial needs to be calculated.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n-1)  # Recursive case: n * factorial of (n-1)

# Get the input number from the command-line argument, convert it to an integer, and calculate its factorial.
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)
