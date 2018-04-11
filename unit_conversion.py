#Siddharth Srinivasan
#Lab Section 061
import math

print("Welcome to the length conversion wizard")
print("This program can convert between any of the following units")
print("inches")
print("feet")
print("yards")
print("miles")
print("leagues")
print("centimeters")
print("decimeters")
print("meters")
print("decameters")
print("hectometers")
print("kilometers")
print("Note: you must enter the units exactly as spelled above\n")
val = float(input("Enter Value:\n")) #user input of number to convert
units_in = input("Enter from units:\n") #input of units the number is in
units_out = input("Enter to units:\n") #unit to convert to
SI = {'centimeters': 1, 'decimeter': 10, 'meters': 100, 'decameters': 1000, 'hectometers': 10000, 'kilometers': 100000, 'inches': 2.54, 'feet': 30.48, 'yards': 91.44, 'miles': 160934, 'leagues': 482802}
def convertSI(val, units_in, units_out):
    return round(val*SI[units_in]/SI[units_out], 4) # convert number based on unit
print(val, units_in, "is", convertSI(val, units_in, units_out), units_out) #print result