#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs.")
    result = 1
    while n > 1:
        result *= n
        n -= 1  
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <nombre>")
    else:
        try:
            f = factorial(int(sys.argv[1]))
            print(f)
        except ValueError as e:
            print(f"Erreur : {e}")
