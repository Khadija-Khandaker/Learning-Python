# The game() function in a program lels a wer blay a game and returns the scote as an integer. You need to read a file 'Histere txt' which is either blank or contams the previous Hi-Score. You need to write a program to update the Hi-Sime Whenever gamel) breaks the Hi-Score.
import random
import os

def game():
    print("You are playing the game.")
    score = random.randint(1, 62)

    # Fetch the high score
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"Your score: {score}")
    if(score>highscore):
    # write this hiscore to the file
        with open("highscore.txt", "w") as f:
            f.write(str(score))

    return score

game()             

 
 
