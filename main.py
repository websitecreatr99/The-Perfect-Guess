import random
randNumber = random.randint(1, 101)

userguess = None
guesses = 0

while(userguess != randNumber):
    userguess = int(input("Enter your number:  "))
    guesses += 1
    if (randNumber == userguess):
        print("You have guess right!")
    else:
        if(userguess > randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())
if(guesses < hiscore):
    print(" You have created an hiscore!!! ")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))