# https://stackoverflow.com/questions/21809112/what-does-tuple-and-dict-mean-in-python
x, y, z = (1, 2, 3)
print(x, y, z)
print("-------------------------------")
# x, y = (1, 2, 3)
# print(x, y) -----> we get an error here, ValueError: too many values to unpack (expected 2)

# x, y, z = *(1, 2, 3) -----> we get an error here, SyntaxError: can't use starred expression here
# print(x, y, z)

# unpacking list or tuple into multiple variables
x, *xs = (1, 2, 3, 4)
print(x)  # 1
print(xs)  # [2, 3, 4]

*xs, x = (1, 2, 3, 4)
print(xs)  # [1, 2, 3]
print(x)  # 4

x, *xs, y = (1, 2, 3, 4)
print(x)  # 1
print(xs)  # [2,3]
print(y)  # 4
print("-------------------------------")

# merging two lists
a = [1, 2, 3]
b = [4, 5, 6]
c = [*a, *b]
print(c)
print("-------------------------------")

# Magical Gacha or using just star as argument
# Note that parameters that appear after a "*"" are keyword-only:

# def f(a, *, b): ...
# f(1, b=2)  # fine
# f(1, 2)    # error: b is keyword-only

# The * indicates the end of the positional arguments. Every argument after that can only be specified by keyword.
# for more info click the link in line 1
