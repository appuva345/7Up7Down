#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
from random import randint

money = int(input(
    "Welcome you, 7 Up 7 Down is a dice game which is played by betting on numbers more than 7 or less than 7.\nTwo dies are rolled in the game and if addition of numbers on both the dices matches your bet then the player wins the bet.\n\nHow much money you want to withdraw from your bank?   "))

play = input("Do you want to play a game of 7 Up 7 Down? Y or N?   ")
while play.lower().startswith('y'):
    number = randint(1, 12)
    bet = int(input("For how much money you want to bet for?   "))
    if bet > money:
        print("Foul! Not enough money, you need extra", bet - money,
              "rupees to place the bet, withdraw enough money next time.")
        break

    guess = input(
        "Bet from the following\nNote that if you win the bet for lucky 7 then you will get double the amount of your bet\nbut if you lose you will lose double the amount of the bet.\nA. 7 Up\nB. 7 Down\nC. Lucky 7\nPress A, B or C   ")

    time.sleep(1)
    print(".....")
    time.sleep(1)
    print("Dies are rolling...")
    time.sleep(1)
    print(".....")
    time.sleep(1)
    print(".....")
    time.sleep(1)

    if guess.lower().startswith('a'):
        if number > 7:
            print("You have guessed correctly! The number was", number)
            money = money + bet
            print("You have", money, "rupees.")
            play = input("Play again? Y or N   ")
            if money < 1:
                print("You have run out of money, time to go to the ATM")
                money = int(input("How much money you want to withdraw from your bank?   "))

        if number < 8:
            print("You have guessed wrong! The number was", number)
            money = money - bet
            print("You have", money, "rupees.")
            play = input("Play again? Y or N   ")
            if money < 1:
                print("You have run out of money, time to go to the ATM")
                money = int(input("How much money you want to withdraw from your bank?   "))

    if guess.lower().startswith('b'):
        if number < 7:
            print("You have guessed correctly! The number was", number)
            money = money + bet
            print("You have", money, "rupees.")
            play = input("Play again? Y or N   ")
            if money < 1:
                print("You have run out of money, time to go to the ATM")
                money = int(input("How much money you want to withdraw from your bank?   "))

        if number > 6:
            print("You have guessed wrong! The number was", number)
            money = money - bet
            print("You have", money, "rupees.")
            play = input("Play again? Y or N   ")
            if money < 1:
                print("You have run out of money, time to go to the ATM")
                money = int(input("How much money you want to withdraw from your bank?   "))

    if guess.lower().startswith('c'):
        if number == 7:
            print("You have guessed correctly! The number was", number)
            money = money + (bet * 2)
            print("You have", money, "rupees.")
            play = input("Play again? Y or N   ")
            if money < 1:
                print("You have run out of money, time to go to the ATM")
                money = int(input("How much money you want to withdraw from your bank?   "))

        if number != 7:
            print("You have guessed wrong! The number was", number)
            money = money - (bet * 2)
            print("You have", money, "rupees.")
            play = input("Play again? Y or N   ")
            if money < 1:
                print("You have run out of money, time to go to the ATM")
                money = int(input("How much money you want to withdraw from your bank?   "))

print()
print("Okay, the game is over.")
print("You finished with", money, "rupees.")



