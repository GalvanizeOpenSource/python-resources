import sys

total = int(raw_input("""You're going to play a game against the computer. You'll 
first enter a number from 0 to 100, and then the game will begin! You'll trade 
off turns with the computer, and at each turn you'll enter a 1 or a 2. If a 1, 
then 1 will be subtracted from the number, and if 2, then 2 will be subtracted 
from the number. The computer is going to have a built in strategy that will 
aim to beat you! To begin, please enter a number from 1 to 100: \n"""))

print "The total we're starting off with is: {} .\n".format(total)

while True: 
    n = total % 3
    if not n: 
        total -= n
        print "The computer plays a {} .\n".format(n)
    else: 
        total -= 1
        print "The computer plays a 1 .\n"

    print "The total after the computer's turn is: {} \n".format(total)

    if not total: 
        print "The computer wins!"
        sys.exit(0)
    else: 
        play = 0
        while (play != 1 and play != 2): 
            play = int(raw_input("Your turn! Do you want to subtract a 1 or a 2?"))
        total -= play
        if not total: 
            print "You win!"
            sys.exit(0)
