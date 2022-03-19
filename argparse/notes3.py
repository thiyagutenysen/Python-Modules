# we will change the usual code in notes2 into argparse cli code
import argparse
import sys


def calculate(x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        return x / y


if __name__ == "__main__":

    # argparse block
    ############################################################################
    # initialize parser
    parser = argparse.ArgumentParser()

    # 4 arguments are required
    # 1. --variable_name is the convention. "--" is a must for optional parameters
    # 2. input type of the variable, such that only this type is accepted and others throw error
    # 3. default value, if the user doesn't wanna provide this variable
    # 4. helper statement to tell us what this variable is about and what it does to sort of give us an idea
    parser.add_argument(
        "--x", type=float, default=1.0, help="What is the first number?"
    )
    parser.add_argument(
        "--y", type=float, default=1.0, help="What is the second number?"
    )
    parser.add_argument(
        "--operation",
        type=str,
        default="add",
        help="What operation? ('add', 'subtract', 'multiply', 'divide')",
    )

    args = (
        parser.parse_args()
    )  # this returns abstract data object that contains all the variables
    x = args.x
    y = args.y
    operation = args.operation
    ############################################################################

    # most safest way to return output to command line
    sys.stdout.write(str(calculate(x, y, operation)))

# Interaction with CLI
# 1st essential command
# this below 1st command prints the help statements for each variable that were defined above,
# to give us idea about the program inputs and it's very useful to start with
# 1. python notes3.py -h

# 2. python notes3.py                                  -----> this uses default values for all variables
# 3. python notes3.py --x=3                            -----> this uses given value for x and default value for others
# 4. python notes3.py --x=3 --operation=divide         -----> this uses given value for x and operation and default value for y
# 5. python notes3.py --x=3 --operation=divide --y=2   -----> this uses all given values, the variables need not be in order
# 6. python notes3.py --x 3 --operation divide --y 2   -----> this is valid too. instead of "=" we can use space

# python notes3.py --x =3 --operation =divide --y =2     |
# python notes3.py --x= 3 --operation= divide --y= 2     | ----> all these 3 commands won't work because command line hates spaces
# python notes3.py --x = 3 --operation = divide --y = 2  |
