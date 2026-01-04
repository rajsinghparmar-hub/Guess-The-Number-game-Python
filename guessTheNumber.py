import random as ran
target = ran.randint(1, 100)

while True:
    usrChoice = input("Guess the target or quit(Q): ")
    if usrChoice == "Q":
        break
    usrChoice = int(usrChoice)
    if usrChoice == target:
        print("Success: correct guess")
        break
    elif usrChoice < target:
        print("your number was too small, take a bigger guess: ")
    else: 
        print("your number is too big, take a small guess: ")
print("Game over")
