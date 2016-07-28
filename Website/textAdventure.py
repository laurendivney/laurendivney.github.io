start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
'''


print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
done = False
while done == False:
    if user_input == "left":
        print("You decide to go left and you run into a bear.")
        choice = 1
        done = True
    elif user_input == "right":
        print("You choose to go right and you reach a river.")
        choice = 2
        done = True
    else:
        user_input = input("please type in either 'left' or 'right'")
    

if choice == 1:
    print("Will you fight it or run away?")
    user_input = input()
    done = False
    while done == False:
        if user_input == "fight":
            choice = 3
            print("After hours of fighting, you finally win so you keep going!")
            done = True
        elif user_input == "run":
            choice = 4
            print("You have decided to run away.")
            done = True
        else:
            user_input = input("please type in either 'fight' or 'run'")

if choice == 3:
    print("You come across a piece of cheese. Will you ignore it or eat it?")
    user_input = input()
    done = False
    while done == False:
        if user_input == "eat":
            choice = 9
            print("it tastes good but you die three munites later since you accidentally touched the walls of the maze while you were fighting the bear.")
            done = True
        elif user_input == "ignore":
            choice = 10
            print("you made the smart move to ignore it but you die three minutes later since you accidentally touched the walls of the maze while you were fighting the bear.")
            done = True
        else:
            user_input = input("please type in either 'eat' or 'ignore'")


if choice == 2:
    print("You end up at the river and run into a ton of rats. Will you swim or fight?")
    user_input = input()
    done = False
    while done == False:
        if user_input == "swim":
            choice = 5
            print("there was a shark in the water and you died.")
            done = True
        elif user_input == "fight":
            choice = 6
            print("the rats bite your face off and you die!")
            done = True
        else:
            user_input = input("please type in either 'swim' or 'fight'")


if choice == 4:
    print("Eventually, you reach a unicorn and a pegasus. Choose only one.")
    user_input = input()
    done = False
    while done == False:
        if user_input == "unicorn":
            choice = 7
            print("the unicorn was actually an evil spirit in disguise. You died.")
            done = True
        elif user_input == "pegasus":
            choice = 8
            print("the pegasus flew out of the maze and over to safety!")
            done = True
        else:
            user_input = input("please type in either 'unicorn' or 'pegasus'")
        print("The game is now over")
    
