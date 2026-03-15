import random 
n = random.randint(1, 100)
guess_number = -1

guess = 0
while guess_number != n:
    guess_number = int(input("Guess the number :"))
    if guess_number < n:
        print("guess a higher number")
    elif guess_number > n:
             print("guess a lower number")
    guess += 1
print(f'You guessed the number {n} in {guess} guesses.')
print("Game Over")
