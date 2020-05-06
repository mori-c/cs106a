"""
Write a program to simulate a magic eight ball. The program should
let the user type a yes or no question and pick a random answer from a
set of 6 predetermined answers.
"""
import random

def main():

    # get user's question
    user_question = input("Ask a yes or no question: ")

    while user_question != '':
        """
        Quick review of comparison operators:
        comparison operators: == or !=
        = is the assignment operator and not the comparison operator
        e.g. user_question == 'Chris', num_students != 7
        
        while user still has questions to input, keep doing the following
        """

        # random.randint is a function that randomly picks an integer within the numbers provided
        choice = random.randint(1, 3)

        if choice == 1:
            # this code will run only if the condition above is TRUE (which means dice is equal to 1)
            print("Outlook good")

        if choice == 2:
            # this code will run only if the condition above is TRUE (which means dice is equal to 2)
            print("Very doubtful")

        if choice == 3:
            print("Without a doubt")

        # ask the user for a question again
        # if missing the line below, will go into infinite loop since user_question will never be empty
        user_question = input("Ask a yes or no question: ")


if __name__ == '__main__':
    main()