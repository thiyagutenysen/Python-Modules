a = {"1": 2, "2": 3, "3": 4}
print(a)
print(*a)  # dictionary is unpacked into just keys, values are ignored
# print(**a)  # -----> this gives us an error, TypeError: '1' is an invalid keyword argument for print()
# **kwargs is not the same as *args, as we get error while printing
print("----------------------------------------")

# usecase example
def foo(x, y):
    print(x, y)


d = {"x": 1, "y": 2}
foo(**d)
