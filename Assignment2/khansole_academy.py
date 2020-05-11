import random

total = 0
pass_count = []

def main():
  play_game()


'''
Helper Functions
'''
def question():
  min = 1
  max = 99
  num1 = random.randint(min, max)
  num2 = random.randint(min, max)
  total = num1 + num2
  print('What is ' + str(num1) + ' + ' + str(num2) + '?')
  print(total)

def answer():
  input_answer = int(input('Your answer: '))
  print(input_answer)


def correct():
  if total == input_answer:
    # if True, add 'passed' into pass_count list
    pass_count += 1
    print('\n Correct! You\'ve gotten -' + str(count_pass()) + '- correct in a row.')

def incorrect():
  if not (int(total) == int(input_answer)):
    pass_count = 0
    print('Incorrect. The expected answer is ' + str(total))

def validate():
  if correct():
    pass_check()
  else:
    incorrect()
    print(failed)

def game_check():
    if (pass_check == 3):
      print('Congratulations! You mastered addition.')
    else:
      # print('not gameover yet')
      play_game()

def play_game():
  main()
  # question()
  # answer()
  # validate()
  # game_check()





if __name__ == '__main__':
    main()