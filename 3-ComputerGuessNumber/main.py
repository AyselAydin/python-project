import random

def computer_guess(num):
    start, end = 1, 100
    back = ''
    while back != "c":
        if start <= end:
            guess = random.randint(start, end)
        else:
            guess = start

        back = input(f"Is {guess} if greater than the value you have in mind (h), if lower (l), if correct (c). If you want to exit the game, press any key.").lower()
        if back == 'h':
            end = guess - 1
        elif back == 'l':
            start = guess + 1
        elif back != 'c':
            print("You are leaving the game!")
            break
    else:
        print('Congratulations, correct guess!')

computer_guess(9)