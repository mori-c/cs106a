"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    print('This program subtracts one number from another.')
    num1 = input('Enter first number: ')
    num1 = int(num1)
    num2 = input('Enter second number: ')
    num2 = int(num2)
    total = str(num1 - num2)
    # total = str(total)
    print('The result is ' + total)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
