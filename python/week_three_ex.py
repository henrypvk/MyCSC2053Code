# name = input("What is your name? ")
# print(name)
#
# while True:
#     age = input("How old are you? ")
#     try:
#         age = int(age)
#         age += 1
#         print("Next year you will be", age)
#         break
#     except ValueError:
#         print("You must enter a number")
#         continue
#
# print("arg1", "arg2", end=', ', sep=', ')
# print("arg3", "arg4", sep=', ')

# file = open("top_ten_movies.txt")
# text = file.read()
# print(text)

# with open("top_ten_movies.txt") as file:
#     for line in file:
#         line = line.rstrip()
#         print(line)

# movies =[]
# with open("movies_only.txt") as file:
#     for line in file:
#         movies.append(line.rstrip())
#         print(movies)
#
# data = "Jose Lopez 60"
# new_data = data.split()
# name = new_data[0] + " " + new_data[1]
# height = int(new_data[2])

# name_height = {}
# with open("heights.txt") as file:
#     for line in file:
#         new_data = line.split()
#         name_height[new_data[0] + " " + new_data[1]] = int(new_data[2])
#
# print(name_height)
number = 1
number = number.lower()
