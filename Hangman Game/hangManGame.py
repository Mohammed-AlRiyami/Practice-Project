from wordList import words
import random
import string

word = random.choice(words).upper() # Getting a ronadom from a words list


def hangman():
    
    lives = 5 # the player gets five tries to guess the right word!
    
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    # The loop is the fundamental part of the game
    while len(word_letters) > 0 and lives > 0:
        print("You have used these letters: ",' '.join(used_letters))
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: "," ".join(word_list)) 
        
        # This line gets the user guessed letter
        user_input = input("Please enter a letter: ").upper()
        if user_input in (alphabet - used_letters):
            used_letters.add(user_input)
            # The if statement checks if the inputted letter is valid else is substracts a life
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives -= 1
                print("Oops wrong guess, you have ", lives, " lives left!")
        elif user_input in used_letters:
            print("You already used the letter! use another letter.")
        else: 
            print("Invalid character.")
        
    if lives == 0: 
        print("You failed to guess the right word, all the best next time!")
    else: 
        print("Congratulations, you guessed the word: ", word)
    
hangman() # Game starts here