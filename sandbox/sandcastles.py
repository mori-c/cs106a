"""
File: sandcastles.py
-------------------------
Practice of control flow, variable and function concepts using the following files:
1 - subtract_numbers.py
2 - random_numbers.py
3 - liftoff.py
"""
import random
import array


def main():
    """
    Part 1
		- user inputs numbers, py separates numbers with substracton operator
				- input(42)
				- int(input)
				- print(4-2)
    """
		print('Let\'s start a program. You\'ll be entering 2 numbers where one number subtracts from another.')
		num1 = input('Enter first number: ')
		num1 = int(num1)
		num2 = input('Enter second number: ')
		num2 = int(num2)
		total = num1 - num2
		total = str(total)
		print('Your result is ' + total)

		"""
		Part 2
		- print 10 random intergers between 0 and 100
				- random.randint() -> generate random numbers
				- print rand(10)
				- NUM_RANDOM -> randomizes 10 numbers
				- MIN_RANDOM
				- MAX_RANDOM
		"""
		min_random = 0
		max_random = 100

		for i in range(10):
				num_random = random.randint(min_random, max_random)
				print(num_random)

		"""
		Part 3
		- spaceship launch
				- reserve print from 10 to 1
				- print('Liftoff!')
				- for i in range()
		"""
		success = 'Liftoff!'

		def countdown():
				# for i in reversed(range(1, max_count + 1)):
				for i in range(10, 0, -1):
						print(i)
				# print(success)

		countdown()
		print(success)




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

