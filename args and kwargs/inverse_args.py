# inverse args is just my own definition for unpacking lists or tuples using "*"
array1 = [1, 2, 3, 4, 5]
print(array1)
print(*array1)  # here we un-bundle the single unit into it's independent elements
array2 = ("a", "b", "c", "d")
print(array2)
print(*array2)  # here we un-bundle the single unit into it's independent elements

# usecase example
x = [1, 2, 3]
y = [2, 1, 3]
graph = (x, y)
import matplotlib.pyplot as plt

# plt.plot(x, y) -----> this is the usual syntax
plt.plot(
    *graph
)  # we get the same graph as the above one, bcz this line is same as plt.plot(x, y)
plt.show()

