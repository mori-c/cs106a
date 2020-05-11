import random

pass_count = 0

def main():
  question()
  answer()
  validate()
  game_check()

'''
Helper Functions
'''
def question():
  global total
  min = 1
  max = 99
  num1 = random.randint(min, max)
  num2 = random.randint(min, max)
  total = num1 + num2
  print('What is ' + str(num1) + ' + ' + str(num2) + '?')
  print(total)

def answer():
  global input_answer
  input_answer = int(input('Your answer: '))
  print(input_answer)

def validate():
  global pass_count
  # correct
  if total == input_answer:
    pass_count += 1
    print('\n Correct! You\'ve gotten ' + str(pass_count) + ' correct in a row. \n \n')
  #incorrect, if total != input_answer
  else:
    pass_count = 0
    print('Incorrect. The expected answer is ' + str(total))

def game_check():
    if (pass_count == 3):
      print('Congratulations! You mastered addition.')
    else:
      play_game()

def play_game():
  main()


if __name__ == '__main__':
  main()