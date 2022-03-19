dictionary = dict()
dictionary["hello"] = "what"
array = [1, 2, 3, 4, 5]

print(dictionary)
print(*dictionary)
print(array)
print(*array)
print(**array)  # we get error
print(**dictionary)  # we get error

