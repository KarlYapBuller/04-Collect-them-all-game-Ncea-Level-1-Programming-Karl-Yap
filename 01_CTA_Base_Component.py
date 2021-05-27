#Collect them all game

import random

#Functions

#Played before function, output depends on what the user answers
#If the user answers yes, program continues ask user how many
#Rounds they want to play or if they want to play continuous mode
#If user answers no, game information will display
#If user answers anything other than yes/no, <error> please answer yes/no will appear
def played_before(question):
    valid = False
    while not valid:
        response = input(question).lower()
#If user response is either 'yes' or 'y' the response will be outputed as yes.
        if response == "yes" or response == "y":
            response = "yes"
            return response
#If user response is either 'no' or 'n' the response will be outputed as no.
        elif response == "no" or response == "n":
            response = "no"
            return response
#If user response is anything other than yes or no,user will be asked to answer yes or no.
        else:
            print("<error> please answer yes/no")

#User Game Instructions
#Displayed if the User has not played this game before
def Game_Instructions():
    statement_generator("How to Play", "*")
    print("The aim of this game is to get enough tokens to spell the word coffee.")
    print("These tokens are given when you order a coffee.")
    print("For example, you are asked what coffee you would like.")
    print("The option are out of capachino (c), flatwhite (f), latte (l), expresso (e) or you can input 'xxx' to quit the game.")
    print("Once you have placed your order you will recieve your token and like previously mentioned once you get colleceted the right number of")
    print("tokens to spell the word coffee you will recieve a free coffee and a muffin.")
    return""

#User Choice Checker
def choice_checker(question, valid_list, error_message):

    valid = False
    while not valid:

        #Ask user for choice and puts choice in lowercase
        response = input(question).lower()

        #Iterates through list anf if response is an item
        #In the list (or the first letter of an item),
        #The full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        #Output error if the item is not in the list
        print(error_message)
        print()


#Rounds Checker
def check_rounds():
    while True:
        statement_generator("Get Ready ", "#")
        response = input("Get Ready to start your order, press <Enter> to place your order: ")

        round_error = "<Error> Please type <Enter>"
#If ifinite mode is not chosen, check response is an integer more than 0
        if response == "":
            return ""

        else:
            print(round_error)
            print()
            continue

        return response


#Statement generator
#Decorates the statements in the Lucky Unicorn game
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


#Played before function, output depends on what the user answers
#If the user answers yes, program continues to show the
#Game summary which is in the game_history_statistics function
#If user answers no, User will be thanked for playing the game
#If user answers anything other than yes/no, <error> please answer yes/no will appear
def game_summary_question(question):
    valid = False
    while not valid:
        response = input(question).lower()
#If user response is either 'yes' or 'y' the response will be outputed as yes.
        if response == "yes" or response == "y":
            response = "yes"
            return response
#If user response is either 'no' or 'n' the response will be outputed as no.
        elif response == "no" or response == "n":
            response = "no"
            return response
#If user response is anything other than yes or no,user will be asked to answer yes or no.
        else:
            print("<error> please answer yes/no")

#Game Statistics
def game_history_statistics():

    #Game History
    print()
    statement_generator("Game History", "*")
    for game in game_summary:
        print(game)

    print(number_coffees)

    print()

    return""


#Main Routine


#Welcomes user to the Collect the all game
#Welcome to the 'Collect Them All" \ statement is decorated
statement_generator("Collect them all game", "*")
print()


#Calls ask user if they have played before funtion and game information function
#Played before statement is decorated
#If the user answers yes, program continues to ask the user how much they want to play with
#If user answers no, game information will display
#If user answers anything other than yes/no, <error> please answer yes/no will appear
print()
statement_generator("Played before", "?")
show_played_before = played_before("Have you played this game before (yes/no)? ")
print()

if show_played_before == "no":
    print()
    Game_Instructions()


#Lists for valid input for checking responses
#List for comparing and for tokens
coffee_list = ["capachino", "flatwhite", "latte", "expresso", "xxx"]
coffee_list_user_free_coffee = ["capachino", "flatwhite", "latte", "expresso"]
token_list_generate = ["C", "O", "F", "E"]
token_list_compare = ["C", "O", "F1", "F2", "E1", "E2"]
muffin_list = ["chocolatte", "vanilla", "redvelvet"]

#Open list for the game summary and token history
game_summary = []
token_history = []

#Rounds played
rounds_played = 0


#Displayed to the user to ask the number of rounds the
#User wants to play or if they input <enter> it is a continous number of rounds played
rounds = check_rounds()

game_loop = ""
while game_loop == "":

#Start of the Collect Them All Game

    #Round heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Order {}".format(rounds_played + 1)

    statement_generator(heading, "#")

    #Gets the Users coffee of choice
    coffee_instruction = "What would you like to order the options include " \
                         "\ncapachino (c), flatwhite (f), latte (l), expresso (e) or you can input 'xxx' to quit the game: "

    #If the Users gesture of choice is invalid
    #Error message is displayed to the User and the valid inputs are displayed
    coffee_error = "<Error> Please enter capachino (c), flatwhite (f), latte (l), expresso (e) or you can input " \
                   "'xxx' to quit the game: "

    muffin_instruction = "What would you like to order the options include " \
                         "\nchocolatte (c), vanilla (v) and redvelvet (r): "

    muffin_error = "<Error> Please enter chocolatte (c), vanilla (v) and redvelvet (r): "

    #Ask user for choice and check it is valid
    user_choice = choice_checker(coffee_instruction, coffee_list, coffee_error)

    #End game if exit code is typed
    if user_choice == "xxx":
        break


    #Get Computer Choice from choosing from token_list_generate and generate a random result for the
    #token for the free coffee
    computer_choice = random.choice(token_list_generate)

    #Compare User and Computer Choice
    #If the User Choice is one of the valid drink options the result is the
    #computers rancdom token and the token is equal to that token for the duplicate letters F and E the first time
    #the token is generated it will be F1 or E1 and any time after that if F1 or E1 is in the token history it will be either F1 or E2


    if user_choice == "capachino":
        result = computer_choice

        if result == "C":
            token = "C"

        elif result == "O":
            token = "O"

        elif result == "F":
            token = "F1"
            if token in token_history:
                token = "F2"

        elif result == "E":
            token = "E1"
            if token in token_history:
                token = "E2"

    #Rock beats Scissors
    #Result is outputed to the User that they hay have won the round
    elif user_choice == "flat White":
        result = computer_choice

        if result == "C":
            token = "C"

        elif result == "O":
            token = "O"

        elif result == "F":
            token = "F1"
            if token in token_history:
                token = "F2"

        elif result == "E":
            token = "E1"
            if token in token_history:
                token = "E2"

    elif user_choice == "latte":
        result = computer_choice

        if result == "C":
            token = "C"

        elif result == "O":
            token = "O"

        elif result == "F":
            token = "F1"
            if token in token_history:
                token = "F2"

        elif result == "E":
            token = "E1"
            if token in token_history:
                token = "E2"


    elif user_choice == "expresso":
        result = computer_choice

        if result == "C":
            token = "C"

        elif result == "O":
            token = "O"

        elif result == "F":
            token = "F1"
            if token in token_history:
                token = "F2"

        elif result == "E":
            token = "E1"
            if token in token_history:
                token = "E2"

    #The feedback outputed to the User for each order they have placed
    feedback = "You chose {} the Token is {}. ".format(user_choice.title(), result)

    token_compare_set = set(token_list_compare)

    token_history_set = set(token_history)

    if token_compare_set.issubset(token_history_set):
        print(feedback)
        print("You got enough tokens to spell the word coffee")
        print("That means you get a free random coffee and a muffin of your choice")
        print()
        print("You got a free {}".format(random.choice(coffee_list_user_free_coffee)))
        print()
        user_muffin = choice_checker(muffin_instruction, muffin_list, muffin_error)
        print("The muffin you choice was {}".format(user_muffin))
        break

    #Result outputed to User
    print(feedback)

    #The tokens that the User got to spell the word coffee each order is put into a list
    token_history.append(token)

    #If the User wants to see the Game History
    #The round and the result of the round is displayed
    rounds_result = "Order {}, Coffee Type: {}, Token: {}".format(rounds_played + 1, user_choice, result)

    #The number of coffees it took for the User to order to get enough tokens to spell the
    #word coffee and get a free coffee and muffin once they had enough tokens to spell the word coffee
    number_coffees = "To get the free coffee and muffin you needed {} orders to get the tokens needed to spell coffee".format(rounds_played + 1)

    #Makes the game results go down in a list instead of across in a list
    game_summary.append(rounds_result)

    #Increases the number of rounds played by 1
    rounds_played += 1

#Game History

#Calls game summary question function
#Game Summary statement is decorated
#If the user answers yes, program continues to show the
#User the game summary which includes the game history and statistics
#User will be thanked for playing the game
#If user answers no, User will be thanked for playing the game
#If user answers anything other than yes/no, <error> please answer yes/no will appear
print()
statement_generator("Game Summary", "?")
show_game_summary_question = game_summary_question("Do you want to see your Game Summary (yes/no)? ")
print()

if show_game_summary_question == "yes":
    print()
    game_history_statistics()

#Thanks the User for playing the Collect Them All game
print()
statement_generator("Thank You for playing the Collect Them All game", "*")
