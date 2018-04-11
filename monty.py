# Siddharth Srinivasan
# CS171 061

import math
import random


seed_flag = False
test_flag = False
tests = 0
input_string = ""
seed = 0

while seed_flag == False:
    try:
        seed = int(input("Enter Random Seed:\n"))  #check if input is a number
        seed_flag = True
        random.seed(seed)
    except ValueError:
        print("Seed is not a number!")
        exit()
print("Welcome to Monty Hall Analysis")
print("Enter \"exit\" to quit.")
switch = 0
while test_flag == False:
    try:
        input_string = input("How many tests should we run?\n") # check if input is a number 
        tests = int(input_string)
        test_flag = True
    except ValueError:
        if input_string == "exit":  #if input is "exit" then exit code
            exit()
        else:
            print("Please enter a number.")
            
doors = ['C', 'G', 'G'] #initialize variables
stay_count = 0
switch_count = 0
j = 0

def simulate_game(test_iteration):
    global stay_count #different from local variables
    global switch_count
    random.shuffle(doors)
    player = random.randint(1,3) #pick random int from 1 to 3
    for i in range(3):
        if doors[i] == 'C':
            continue
        elif i == (player-1):
            continue
        else:
            monty_choice = (i+1)
    if tests <= 10: # for long summary
        print("Game", test_iteration+1)
        print("Doors:", doors)
        print("Player selects Door:", player)
        print("Monty selects Door:", monty_choice)
        if doors[player-1] == 'C':
            stay_count = stay_count + 1
            print ("Player should stay to win.") #number of wins for stay
        else:
            switch_count = switch_count + 1 #count number of wins for switch
            print ("Player should switch to win.")
    else:
        if doors[player-1] == 'C':
            stay_count = stay_count + 1
        else:
            switch_count = switch_count +1

while j <= (tests):
    if j < tests:
        simulate_game(j)
        j += 1
    else:
        percent_stay = stay_count/(stay_count+switch_count)*100 #calculate the percent for stay
        percent_switch = (switch_count/(stay_count+switch_count))*100 #calculate the percent for switch
        print("Stay won", percent_stay, "% of the time.")
        print("Switch won", percent_switch, "percent of the time.")
        try:
            stay_count = 0
            switch_count = 0
            j = 0
            input_string = input("How many tests should we run?\n")
            tests = int(input_string)
            test_flag= True
        except:
            if input_string == "exit":
                exit()
            else:
                print("Please enter a number.")


        switch = switch + 1
        print("Player should switch to win.")
j = 0

while j < tests:
    simulate_game()
    j += 1
percent_stay = '{:.1%}'.format(stay/(stay+switch)) 
percent_switch = '{:.1%}'.format(switch/(stay+switch))
print("Stay won", percent_stay, "of the time.")
print("Switch won", percent_switch, "of the time.")
