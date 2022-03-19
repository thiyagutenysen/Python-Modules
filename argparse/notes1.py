# https://www.youtube.com/watch?v=0twL6MXCLdQ
# https://www.youtube.com/watch?v=QILBGC7TApM

# argparse is used to make commandline interfaces

# using command line makes interacting with the program easier.

# we can change variables in command line itself instead of editing code file
# above line is extremely useful if we use someone else's code, bcz
# we won't be able to understand his code and it's difficult for us to search his code for variables to change
# instead if he provides clear documentation on how to change values in command line itself. It would be way easier
# eventhough if he doesn't provide documentation we can ask "python code.py -h" in command line,
# we will get our documentation printed in Command Line if the guy is professional

# it's easy to tweak things and rerun it quickly

# argparse - argument parser
# this module helps us to make command line interactive but not upto the level of gui

# if we use input() method instead of argparse,
# to incorporate default values we need to use "try except" or "or" statements, which is ugly
# argparse seamlessly let's us use default values without any hassle
