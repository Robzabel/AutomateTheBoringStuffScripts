#This is a guess the number game
import random
print("Hello, what is your name?")
name = input()
print("Hello " + name + ", Im thinking of a number between 1 and 20")
secretNumber = random.randint(1, 20)

for guessesTaken in range (1,7):
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break #This contition if if they guess the corect answer

if guess == secretNumber:
    print("Good job, you guessed that my secret number was " + str(secretNumber))
    print("You took " + str(guessesTaken) + " Guesses to guess the answer.")
else:
    print("Nope, the number i was thinking of is " + str(secretNumber))