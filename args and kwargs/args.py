# here args take seperate n number of variables or items and bundles them as a list.
# n can be any number.

# true meaning:
# *args = 'a', 'b', 'c'            -----> *args is unpacked items
# args = ['a', 'b', 'c']           -----> args is a list

# example 1
def cast(*args):
    # we loop through the list
    for member in args:
        print(member, end=", ")
    print()


member1 = "charlie"
member2 = "mac"
member3 = "frank"
member4 = "dennis"

cast(member1, member2, member3, member4)
print("----------------------------------------------")
cast(member1, member2, member4)
# the advantage of *args is that it can consume any number of arguments
# function is not hard defined on the number of arguments given in
# *args allow unlimited number of arguments to be passed into the function
print("----------------------------------------------")

# example 2
def show(title, *args):
    print(title)
    print("cast = ", end="")
    for member in args:
        print(member, end=", ")
    print()


show("it's always sunny in philadelphia", member1, member2, member4)
# python automatically know that the first argument belongs to title variable,
# and all the upcoming arguments belongs to args variable
