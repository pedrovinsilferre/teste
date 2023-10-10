#INPUT

# name = input('what is your name?')


# color = input('what is your favorite color?')
# animal = input('what is your favorite animal?')

# print('{}, you like a {} {}!'.format(name, color, animal))


#ARRAYS
# myFruitsList = ["apple", "banana", "cherry"]
# print(myFruitsList)
# print(type(myFruitsList))
# print(myFruitsList[0])
# myFruitsList[0] = "abacate"
# print(myFruitsList)

#DICIONARIOS

# myFavoriteGames = {
#     "atual" : "valorant",
#     "infancia" : "Metal Gear Solid 3",
#     "daVida" : " TES-V"
# }
# print(myFavoriteGames["daVida"])


#LOOPS-FOR
# mixedList = [8991, True, "ordeP"]

# for item in mixedList:
#     print("{} is of the data type {}".format(item, type(item)))

# import csv
# import copy

# myVehicle = {
#     "vin":"",
#     "make": "",
#     "model": "",
#     "year": 0,
#     "range": 0,
#     "topSpeed": 0,
#     "zeroSisty": 0.0,
#     "mileage": 0
# }

# for key, value in myVehicle.items():
#     print("{} : {}".format(key, value))

#uso de um loop em while

print("welcome to guess the number!")
print("the rules are simple. I will think of a number, and you will try to guess it.")

import random

number = random.randint(1, 10)
isGuessRight = False;

while isGuessRight != True:
    guess = input("guess a number berween 1 and 10: ")
    if int(guess) == number:
        print("you guessed {}. that is correct! you win".format(guess))
    else:
        print("you guessed {}. sorry, that ins't it. try again".format(guess))