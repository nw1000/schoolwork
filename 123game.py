from random import randint

num = randint(10, 50)
playing = True

player1 = input("enter your name player 1: ")

player2 = input("enter your name player 2: ")
while(playing):
    player1Num = int(input(f"{player1} Enter 1 2 or 3"))
    num = num - player1Num
    if (num <= 0):
        print(f"{player1} you loose")
        playing = False

    player2Num = int(input(f"{player2} Enter 1 2 or 3"))
    num = num - player2Num
    if (num <= 0):
        print(f"{player2} you loose")
        playing = False