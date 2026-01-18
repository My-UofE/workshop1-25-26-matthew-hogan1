import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    
    poss_values.sort()

    return poss_values[len(poss_values)//2]

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    
    if next_val < current_val and user_input == 'l':

        return True 

    elif next_val > current_val and user_input == 'h':

        return True 

    return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    
    letterfound = False
    for i,wordletter in enumerate(word):
        
        if letter == wordletter:
            letterfound = True
            board[i] = letter 

    
    if letterfound == True:

        print(f"Well done! '{letter}' is in the word")
        return True

    print(f"Sorry, '{letter}' is not in the word")
    return False
    
            
