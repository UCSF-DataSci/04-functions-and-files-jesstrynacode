#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, 
and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""
# function to check if a number is prime 
# prime number is a whole number > 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).
def is_prime(n):
    if n <= 1: #numbers that are negative, 0, 1 are not prime
        return False
    if n == 2 or n == 3: #2 is smallest even prime number, 3 is smallest odd prime number
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5 #start the loop at 5 (first prime number greater than 3)
    while i * i <= n: #uses the property that all prime numbers fall in the 6k +/-1
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

import argparse

#import the Fibonacci generating function 
from fibonnaci import gen_fibonacci

# Main program to find the largest prime Fibonacci number
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", type=int, help="The upper limit for the Fibonacci numbers.")
    args = parser.parse_args()
    
    fibonacci_numbers = gen_fibonacci(args.limit) #generate Fibonacci numbers up to the limit specified

    prime_fibonacci_numbers = [num for num in fibonacci_numbers if is_prime(num)] #Get the prime Fibonacci numbers

    # Find and print the largest prime Fibonacci number
    if prime_fibonacci_numbers:
        largest_prime_fibonacci = max(prime_fibonacci_numbers)
        print(f"The largest prime Fibonacci number less than {args.limit} is: {largest_prime_fibonacci}")
    else:
        print(f"There are no prime Fibonacci numbers less than {args.limit}.")

