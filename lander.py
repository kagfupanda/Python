##################
# Siddharth Srinivasan
##################

##################
# import re (regular expression) for validating input
# and sys for exiting the prgogram
##################
import sys
import re

##################
# gloabl variables initialized
##################
altitude = 50
velocity = 0.0
thrusterAccl = 0.10
levelIndex = 1 # current user level tracker
oldlevelIndex = 0 # previous user level tracker
success_landing = False # user played level successfully or not
quit = False # did user chose to quit or not

def is_int(val):
    if type(val) == int:
        return True
    else:
        if val.isdigit():
            return True
        else:
            return False
        
##################
# This function prompts user to enter a fuel value.
# Only value it accepts is an integer. If the value entered
# is greater than the current_fuel level, it does not take it
# and continues to prompt for user entry
# return value=fuel to use
##################
def ask_fuel(current_fuel):
    my_string = "Enter unit of fuel to use: \n"
    prompt = "Enter unit of fuel to use: \n"
    while True :
        try:
            ans1 = input(prompt)
            ans1 = int(ans1)
            if int(ans1) > current_fuel:
                prompt = "No enough fuel. Max fuel: " + str(current_fuel) + "\n" + my_string
                continue
            if int(ans1) < 0:
                prompt = "Cannot use negative fuel.\n" + my_string
                continue
            break
        except ValueError:
            prompt="Please Enter Integer Value.\n" + my_string
    
        
    fb = int(ans1)
    return fb

##################
# This function plays a particular level which is denoted by a planet
# For example: level 1 = Moon, level 2 = Earth, level 3 = Pluto etc.
# input: takes name of planet, gravity in the planet, starting fuel level
# return nothing to the caller
# To begin with, prints the initial values for altitude, velocity, current_fuel
# Then prompts user for fuel input to travel,
# calculates the remaining altitude, velocity based on user fuel input
# if altitude reaches 0, determines if the Landed successfully or crashed
# based on final velocity (bwtween -2 and +2 is success) and
# sets success_landing boolean flag to true or false.
##################
def play_level(name,gravity,fuel_level):
    secs = 1
    global altitude
    global velocity

    # General level banner
    print("Entering Level " + str(levelIndex))
    print("Landing on the " + name)
    print("Gravity is " + str(format(gravity,'.2f')) + " m/s^2")
    print("Initial Altitude: " + str(altitude) + " meters")
    print("Initial Velocity: " + str(format(velocity,'.2f')) + " m/s")
    print("Burning a unit of fuel causes " + str(format(thrusterAccl,'.2f')) + " m/s slowdown")
    print("Initial Fuel Level: " + str(fuel_level) + " units")
    print("\nGO")

    global success_landing
    success_landing = False

    # Play the game until the altitude did not drop to 0 or less
    while altitude > 0.0 :
        fuel_to_burn = ask_fuel(fuel_level)

        fuel_level = fuel_level - fuel_to_burn
        velocity = velocity + gravity + thrusterAccl * fuel_to_burn
        altitude = altitude + velocity
        if (altitude < 0) :
            altitude = 0

        print("After " + str(secs) + " seconds Altitude is " + str(format(altitude,'.2f')) + " meters, " + "velociy is "+ str(format(velocity,'.2f')) + " m/s")
        print("Remaining Fuel: " + str(fuel_level) + " units")
        secs = secs + 1

    # set success_landing based on velocity if between -2 and +2 = true
    if velocity >= -2.0 and velocity <= 2.0 :
        success_landing = True

##################
# reset the global variables in preparation for next level
##################
def reset_variables():
    global altitude
    global velocity
    global thrusterAccl
    global success_landing
    global quit

    # set up default values based on hw3.pdf
    altitude = 50
    velocity = 0.0
    thrusterAccl = 0.10
    # internal flags to keep track of level, quit
    success_landing = False
    quit = False

##################
# Ask user if wants to continue to play or quit
# based on the answer gloabl quit flag is set to true or false
##################
def play_or_quit(message):
    global quit
    global levelIndex
    global oldlevelIndex
    
    print(message)
    if levelIndex <=11: 
        ans2 = input("Do you want to play level " + str(levelIndex) + " (yes/no)\n")
        matchObj = re.search("yes", ans2)
        if not matchObj:
            print("You made to past " + str(oldlevelIndex) + " levels.")
            quit = True
        else :
            reset_variables()
            quit = False

##################
# After user played a level, based on success_landing flag or not
# prompt user to quit, play same level or play next higher up level
##################
def prompt_next():
    global success_landing
    global oldlevelIndex
    global levelIndex # keep track of which level the user is at
    global quit # did user chose to quit or not

    if success_landing:
        levelIndex = levelIndex + 1
        oldlevelIndex = levelIndex - 1
        play_or_quit("Landed Successfully.")
        
    else :
        play_or_quit("Crashed!")
    if quit == True:
        my_exit()
    quit = False
    
##################
# Utility function to exit the program
# when user chooses to quit by answering 'no'
# calls sys.exit to immediately stop the program
##################
def my_exit():
    print ("Thanks for playing.")
    sys.exit()

##################
# Main function calls several other functions to do it's job
# prints welcome message
# if user chooses to play level 1,
# calls play_level("Moon", -1.622, 150) until user lands successfully.
# Then moves to level 2 by calling play_level("Earth", -9.81, 5000)
# until user lands on Earth successfully
# so on and so forth until user reaches Mars which is the last level
# user has option to quit or continue at each level whether lands
# successfully or crashes!
##################
def main():
    global quit
    
    print("Welcome to Lunar Lander Game.")
    prompt = "Do you want to play level " + str(levelIndex) + "? (yes/no)\n"
    ans = input(prompt)
    matchObj = re.search("yes", ans)
    if not matchObj:
        print("Thanks for playing.")
        sys.exit()

    # Level 1; play Moon        
    while levelIndex==1:
        play_level("Moon", -1.622, 150)
        prompt_next()

    # Level 2; play Earth   
    while levelIndex==2:
        play_level("Earth", -9.81, 5000)
        prompt_next()

    # Level 3; play Pluto
    while levelIndex==3:
        play_level("Pluto", -0.42, 1000)
        prompt_next()

    # Level 4; play Neptune
    while levelIndex==4:
        play_level("Neptune", -14.07, 1000)
        prompt_next()

    # Level 5; play Uranus
    while levelIndex==5:
        play_level("Uranus", -10.67, 1000)
        prompt_next()

    # Level 6; play Saturn
    while levelIndex==6:
        play_level("Saturn", -11.08, 1000)
        prompt_next()

    # Level 7; play Jupiter
    while levelIndex==7:
        play_level("Jupiter", -25.95, 1000)
        prompt_next()

    # Level 8; play Mars
    while levelIndex==8:
        play_level("Mars", -3.77, 1000)
        prompt_next()

    # Level 9; play Venus
    while levelIndex==9:
        play_level("Venus", -8.87, 1000)
        prompt_next()

    # Level 10; play Mercury
    while levelIndex==10:
        play_level("Mercury", -3.59, 1000)
        prompt_next()

    # Level 11; play Sun
    while levelIndex==11:
        play_level("Sun", -274.13, 50000)
        prompt_next()
       

##################
# Main program call starts here
##################
main()
