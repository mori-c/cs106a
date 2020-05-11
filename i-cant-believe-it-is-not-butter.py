#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[21]:


min = 1
max = 99

pass_count = []


# In[ ]:


def question():
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)
    total = num1 + num2
    total = str(num1 + num2)

    print('What is ' + str(num1) + ' + ' + str(num2) + '?')
    print(total)

question()


# In[ ]:


def answer():
    input_answer = int(input('Your answer: '))
    print(input_answer)
    
answer()


# In[ ]:





# In[ ]:


def correct():
    if (int(total) == int(input_answer)):
        pass_count.append('passed')
        passed = '\n Correct! You\'ve gotten -' + str(count_pass()) + '- correct in a row.'
        print(passed)

correct()


# In[ ]:


def validate():
    if correct():
        print(passed)
        pass_check()
    else:
#         incorrect()
        # print('next question')
        print(failed)
        
validate()


# In[ ]:


def incorrect():
    if not (int(total) == int(input_answer)):
        failed = 'Incorrect. The expected answer is ' + str(total)
        print(failed)

incorrect()


# In[ ]:


# correct answers 3 in a row, wins the game

# pass_count = []

def game_check():
    pass_check = len(pass_count)
    if (pass_check == 3):
        print('Congratulations! You mastered addition.')
    else:
        print('not gameover yet')
#         play_game()

game_check()


# In[ ]:


def count_pass():
    for i in range(1, 4, 1):
        print(i)
        
count_pass()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




