import random

min = 1
max = 99
total = 0
input

pass_count = []

def main():
	question()
	answer()
	validate()
	game_check()


'''
Helper Functions
'''
def question():
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)
    total = num1 + num2
    total = str(num1 + num2)
    print('What is ' + str(num1) + ' + ' + str(num2) + '?')
    print(total)

def answer():
    input_answer = int(input('Your answer: '))
    print(input_answer)


def correct():
	if (int(total) == int(input_answer)):
		# if True, add 'passed' into pass_count list
		pass_count.append('passed')
		passed = '\n Correct! You\'ve gotten -' + str(count_pass()) + '- correct in a row.'
		print(passed)

def incorrect():
	if not (int(total) == int(input_answer)):
		failed = 'Incorrect. The expected answer is ' + str(total)
		print(failed)

def validate():
	if correct():
		print(passed)
		pass_check()
	else:
		# incorrect()
		print(failed)


# winning the game
def game_check():
    pass_check = len(pass_count)
	# check if answers have passed 3 times in a row by verifying appended list length as True
    if (pass_check == 3):
        print('Congratulations! You mastered addition.')
    else:
        # print('not gameover yet')
        play_game()






if __name__ == '__main__':
		main()