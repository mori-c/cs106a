player = [1, 2]
player_1 = ['Player 1']
player_2 = ['Player 2']

stones_1 = []
stones_2 = []

def main():
	while player:
		max_count = 20

		for i in player_1:
			remainder = max_count - sum(stones_1)

			print('There are {} stones left \n'.format(max_count - sum(stones_1)))
			input_answer = int(input('{} would you like to remove 1 or 2 stones? '.format(i)))
			stones_1.append(input_answer)
			# print(stones_1)

			if max_count - sum(stones_1) == 0:
				print('{} Wins!'.format(i))
				return True

		for i in player_2:
			remainder = max_count - sum(stones_2)

			print('There are {} stones left \n'.format(max_count - sum(stones_2)))
			input_answer = int(input('{} would you like to remove 1 or 2 stones? '.format(i)))
			stones_2.append(input_answer)
			# print(stones_2)

			if max_count - sum(stones_2) == 0:
				print('{} Wins!'.format(i))
				return True


if __name__ == '__main__':
	main()
