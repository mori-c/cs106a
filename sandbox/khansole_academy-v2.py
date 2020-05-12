import random

# random_number assignment and reset
min_random = 1
max_random = 99

def num1():
		num1 = random.randint(min_random, max_random)

def num2():
		num2 = random.randint(min_random, max_random)


def main():
		# while play_to_win():

		# question()
				num1 = random.randint(min_random, max_random)
				num2 = random.randint(min_random, max_random)

				print('What is ' + str(num1) + '+' + str(num2) + '?')

				total = num1() + num2()
				total = str(total)


		input_answer = input('Your answer: ')
		input_answer = int(input_answer)

		response()
				# validate()
				#correct
				if total == input_answer:
						print('Correct! You\'ve gotten ' + count_pass() + 'correct in a row.')
				# incorrect
				else:
						not (total == input_answer):
								print('Incorrect. The expected answer is ' + str(total))


		congrats()
				while
				count_pass()
				print()

'''
Helper Functions
'''

# random_number assignment and reset
min_random = 1
max_random = 99

def num1():
		num1 = random.randint(min_random, max_random)

def num2():
		num2 = random.randint(min_random, max_random)


# def addition():
# 		total = num1() + num2()
# 		total = str(total)

def question_index():
		for i in range(8):
				print(i, question())

# q+a validation
validate()
		error()
		correct()

def count_pass():
		for i in range(1, 4, 1):
				print(i)

# three_passes():
# 		if count

did_they_pass():
		if count_pass = 3:
				print(congrats)
		else:
				question()





if __name__ == '__main__':
		main()