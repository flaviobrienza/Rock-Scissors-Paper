import time 
import random
actions = 'Rock', 'Scissors', 'Paper' 

def game():
    question = input('Do you want to play? (pick yes or no) ')
    if question == 'yes':
        print("Let's start, wait 3 seconds")
        time.sleep(1) 
        countdown()
        return random.choice(actions)
    if question == 'no':
        return 'Goodbye'
    else:
        return 'Please restart and enter a valid input (yes or no)'

def countdown():
    for j in range(3, 0, -1):
        print(j) 
        time.sleep(1) 

print(game()) 