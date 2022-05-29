import random

def guess(num):
    count = 0
    random_number = 0
    while num != random_number:
        random_number = int(input("Let's take a guess: "))
        if num < random_number:
            print("Sorry, take a smaller guess.")
        elif num > random_number:
            print("Sorry, take a bigger guess.")
        count += 1
        
    if count == 1:
        print("Congratulations, you got it right on the first try. You are really good at this game.")
    elif count < 6:
        print("Congratulations, you're not bad")
    else:
        print(f"You got it on the {count} guess. I guess you are not good at this game.")

guess(random.randint(1, 100))