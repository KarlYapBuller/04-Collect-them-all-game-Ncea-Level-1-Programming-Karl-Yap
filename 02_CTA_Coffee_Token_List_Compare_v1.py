#Game History

import random

game_summary = []

rounds_played = 10

coffee_list = ["C", "O", "F1", "F2", "E1", "E2"]

for item in range(0, 10):
    result = input("Token: ")

    if result == "C":
        token = "C"

    elif result == "O":
        token = "O"

    elif result == "F1":
        token = "F1"

    elif result == "F":
        token = "F1"
        if token in game_summary:
            token = "F2"

    elif result == "E":
        token = "E1"
        if token in game_summary:
            token = "E2"



    game_summary.append(token)

    set1 = set(coffee_list)

    set2 = set(game_summary)

    if set1.issubset(set2):
        print("You got the tokens to spell coffee")
        break

#Calculate Game Statistics

print()
print("*****Game History*****")
for item in game_summary:
    print(item)


print()

#Displays Game Statistics with percentage (%) values to the nearest whole number

print("*****Game Statistics*****")
print(game_summary)
