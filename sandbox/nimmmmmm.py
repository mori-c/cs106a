"""
File: nimm.py
-------------------------
Alternate stones until zero

1. The game starts with a pile of 20 stones between the players
2. The two players alternate turns
3. On a given turn, a player may take either 1 or 2 stone from the center pile
4. The two players continue until the center pile has run out of stones.

"""

# x == stone count
player = {'Player 1':[], 'Player 2':[]}
# player[0]
# player[1]
input_answer = 0
remainder = 0


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    global input
    max_count = 20
    # min_count = 0
    # stone_count = max_count - input_answer
    print('There are  ' + str(max_count) + ' stones left')

    # input_answer()
    for i in range(2):
        if player['1']:
            input_answer = int(input(player['1'] + ', would you like to remove 1 or 2 stones? '))
            print(str(input_answer))
            remainder = max_count - input_answer
            print('remainder :', remainder)
            print('There are  ' + str(max_count - remainder) + ' stones left')


            player[0].append(input_answer)
            print('player[0]: ', player[0])
        else:
            input_answer = int(input(player[i] + ', would you like to remove 1 or 2 stones? '))
            print(str(input_answer))

    # keep_track()
    if input_answer < max:
        player[0].append(input_answer)
        print('player[0]: ', player[0])
        remainder = max - input_answer
        print('remainder :', remainder)
    else:
        while input_is_valid:
            if (input_answer == max):
                input = int(input('Please enter 1 or 2: '))
                print('Player ' + input + 'wins! \n Game Over')
            else:
                main()

    # player_id()
    # validate()


'''
Helper Functions
'''

def score_statement():
    pass
    # global stone_count
    # global max
    # max_count = 20
    # min_count = 0
    #
    # # for i in range(max_count, min_count):
    # #     print(i)
    # stone_count = int(max_count) - int(input_answer)
    # print('There are' + str(stone_count) + 'stones left \n')

def input_answer():
    pass
    # global input_answer
    # input_answer = int(input('Would you like to remove 1 or 2 stones? '))
    # if player[i] == player[0]:
    #     print('player[1], input_answer: ', player[1], input_answer)
    # else:
    #     # print(player[i])
    #     # input_answer = int(input('Would you like to remove 1 or 2 stones? ' ))
    #     print('player[2], input_answer: ', player[2], input_answer)

# validate
def keep_track():
    pass
    # if input_answer < max:
    #     player[0].append(input_answer)
    #     print('player[0]: ', player[0])
    #     remainder = max - input_answer
    #     print('remainder :', remainder)
    # else:
    #     while input_is_valid:
    #         if (input_answer == max):
    #             input = int(input('Please enter 1 or 2: '))
    #             print('Player ' + input + 'wins! \n Game Over')
    #         else:
    #             main()

def player_id():
    pass
    # for i in range(2):
    #     if player[i] == player[0]:
    #         print(player[0])
    #     else:
    #         print(player[i])

# def validate():
#     if max < input_answer:
#         score_count +=







# net positive or negative of stone in bucket
# def keep_track():
#     max = 20
#     min = 0
#     player = ['1', '2']
#     while player in range(max, min):
#         print(player)

#     remainder = sum(stone_count - input_answer)
#     print(remainder)


#
# def play_game():
#     main()



# player_1()
# player_2()

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
