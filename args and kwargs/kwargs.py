# here kwargs take n number of argument name and argument value pair and bundles them into a dictionary
# n can be any number

# **kwargs - a = 1, b = 2, c = 3            -----> **kwargs is a unpacked key value pair
# kwargs - {'a': 1, 'b': 2, 'c': 3}         -----> kwargs is a dictionary


def show(title, **kwargs):
    print(title)
    print("cast : ", end="")
    for key in kwargs:
        print(key, "=", kwargs[key], end=", ")
    print()


member1 = "charlie"
member2 = "mac"
member3 = "frank"
member4 = "dennis"
title = "it's always sunny in philadelphia"

# kwargs helps us to pass the argument values with argument names too
# method 11
show(
    title, member1=member1, member2=member2, member4=member4
)  # here with brackets python knows what to consider as argument names and argument values
print("--------------------------------------------------")
# method12
show(title=title, member1=member1, member2=member2, member4=member4)
print("--------------------------------------------------")
# method 2
show(
    title, member1="sweet dee", member2="frank", member3="waitress"
)  # here python knows member1 is argument name and doesn't use the value initialized above

# By default python knows, inside function calls,
# what came before "=" is argument name and what comes after "=" is argument value

