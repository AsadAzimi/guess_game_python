#in this program system guess the number which we chose
import random

def computer_guess(low,high):
    lowt = low
    hight = high
    fedback = ''
    temp = True
    while temp == True:
        g = input(f"Guess a number between {low} to {high} [y,N]: ")
        if g == 'y':
            try:
                while fedback != 'c':
                    if low == high:
                        guess = low
                    else:
                        guess = random.randint(low,high)
                    fedback = input(f"is {guess} too high 'h', is {guess} too low 'l', is {guess} corect 'c': ")
                    if fedback == 'h':
                        high = guess - 1
                    elif fedback == 'l':
                        low = guess + 1
                print(f"Yeh! I guessed Your Number {guess}.")
                temp = False
            except Exception:
                print("I could not guess your number. may be your fedback was wrong.")
                again = input("Do you want to play again [Y,N]? ".lower())
                if again == 'y':
                    temp = True
                    low = lowt
                    high = hight

ask = input("Do you wan to play {Gusse Number}? [Y.N]:".lower())
if ask == 'y':
    low = int(input("Enter the low number: "))
    high = int(input("Enter the high number: "))
    computer_guess(low,high)

