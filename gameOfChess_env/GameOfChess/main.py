from chessman import chessman
from constants import constants
from player import player
from game import game
from board import board
import sys

if __name__ == "__main__":

    # Ask for new players details
    print("Please selct a Color a Name to begin the game. U can select either black or white color.")
    
    print("Its Player 1 time to select.")
    player1_name = input("Name plz : ")
    player1_color = input("Color plz : ")
    
    # print(type(player1_name))
    # p1 = player('a', 'fine')
    player1 = player(player1_name, player1_color)

    print("Its Player 2 time to select.")
    player2_name = input("Name plz : ")

    color_left = ""
    if(player1_color.lower() == "white"):
        color_left = "black" 
    else: 
        color_left = "white" 
    
    print(f"{color_left.capitalize()} color is left to play. Do u accept it ? ")
    player2_acceptance = input("Your Response Y/N : ")
    if(player2_acceptance == "N"):
        print("Terminating game...")
        sys.exit()

    player2 = player(player2_name, color_left)
    
    # start a new game
    game_context = game(board(), player1, player2)
    game_context.start()  

    print("The game has begun : \n", game_context)
    