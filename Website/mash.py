
name = input("What's your name?")


shelter = ["house", "mansion", "appartment", "shack"]

husband = ["Dylan O'Brian", "Dave Franco", "Chris Pine", "Shrek", "no one"]

kids = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

vehicle = ["car", "RV", "ship", "skateboard", "roller skates"]

location = ["California", "New York", "Spain", "Canada", "Russia", "Ohio", "Florida", "Kansas", "Texas"]

career = ["plumber", "actor", "McDonalds worker", "youtuber", "doctor", "teacher"]

import random

print("In the future, " + name + " will be married to " + random.choice(husband) + " and live in a " + random.choice(shelter) + " in " + random.choice(location))
print(" You will drive to your new workplace as a " + random.choice(career) + " in/on a " + random.choice(vehicle) +". You and your husband will have " + random.choice(kids) + " kids and will live happily ever after!")
