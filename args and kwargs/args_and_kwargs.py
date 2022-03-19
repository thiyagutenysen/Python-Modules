def show(title, *args, **kwargs):
    print("Title: ", title)
    print("Episodes: ", end="")
    for episode in args:
        print(episode, end=", ")
    print()
    print("cast: ", end="")
    for character in kwargs:
        print(kwargs[character], "as", character, end=", ")


charlie = "Charlie Day"
mac = "Rob"
dennis = "Glenn"
frank = "danny levito"
title = "it's always sunny in philadelphia"

show(
    title,
    "The Gang Gets Racist",
    "Charlie Wants an Abortion",
    "Underage Drinking: A National Concern",
    "Charlie Has Cancer",
    "Gun Fever",
    "The Gang Finds a Dead Guy",
    "Charlie Got Molested",
    charlie=charlie,
    mac=mac,
    dennis=dennis,
)

