import random
import random_numbers

min_random = 10
max_random = 99

def main():
		def starter_problem():
				# question
				question = 'What is ' + str(rand_1) + ' + ' + str(rand_2) + '?')
				# user input
				answer = input('Your answer: ')
				answer = int(answer)
				def correct():
						if rand_total == answer:
								print('Correct! You\'ve gotten ' + str(correct_count) + ' correct in a row.')
						else:
							print('Incorrect. The expected answer is ' + str(total))


		def next_problem():
				pass

"""
Helper Functions
"""
# random number assignment
for i in range(1):
		rand_1 = random.randint(min_random, max_random)
		rand_2 = random.randint(min_random, max_random)

# generate random numbers
total = rand_1 + rand_2

# 3 problem pass on answering problems correctly
while three_correct_in_row():
		congrats()

if __name__ == '__main__':
		main()