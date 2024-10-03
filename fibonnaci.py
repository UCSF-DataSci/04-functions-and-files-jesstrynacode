#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. 
The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

import argparse

# Fibonacci sequence function
def gen_fibonacci(limit):
    fibonacci_seq = [0, 1]
    while True:
        next_value = fibonacci_seq[-1] + fibonacci_seq[-2]  # Calculates next Fibonacci number
        if next_value >= limit:
            break  # Exit the loop if the next value exceeds the limit
        fibonacci_seq.append(next_value)  # Add the next value to the sequence
    return fibonacci_seq

# Main program to handle file writing
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", type=int, help="The limit for the Fibonacci numbers.")
    parser.add_argument("--filename", "-f", help="The file to write Fibonacci numbers", default="Fibonacci numbers.txt")

    args = parser.parse_args()
  
    fibonacci_numbers = gen_fibonacci(args.limit)  # Generate the Fibonacci numbers

    # write the numbers to the file and handle potential error
    try:
        with open(args.filename, 'w') as f:
            for number in fibonacci_numbers:
                f.write(f"{number}\n")  # Write each Fibonacci number to the file
        print(f"Fibonacci numbers less than {args.limit} have been written to {args.filename}.")
    except IOError as e:
        print(f"Error writing to file: {e}")

