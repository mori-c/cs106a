"""
Write a program to prompt the user for a weight on earth and print
the equivalent weight on the moon.
"""

"""
for style, we make constants all caps
16.5% would not work since % is an operator in Python (aka take the remainder from a division)
"""
MOON_MULTIPLE = 0.165

def main():

    # store the weight inputted by user
    # the input() function always returns a string even if user types in a number (e.g. "8", "8.2")
    earth_weight_string = input("Enter a weight on earth: ")

    # what should we do with user_input?
    # convert user input into a float to prepare for multiplication
    earth_weight_float = float(earth_weight_string)

    # convert to moon weight
    moon_weight = earth_weight_float * MOON_MULTIPLE

    """
    sidebit about variable naming - question from Tomo
    sometimes variable names self-convey their type
    e.g. num_students, num_classes, message, paragraph, text
    """

    # print out the weight to the user
    # if we don't cast moon_weight to a string, will show a concatenation type error
    print("The moon weight is: " + str(moon_weight))

    """
    scratchpad of types
    x = 3     int aka integers
    x = 3.0   # float aka numbers with decimal points
    x = "hello string"
    """


if __name__ == '__main__':
    main()