import random

num = random.randrange(1000, 10000)
n = int(input("Enter a 4 digit number: "))
def mastermind_game(n):
    if n == num:
        print("You guessed the number!")
    else:
        tries = 0
        while n != num:
            tries += 1
            count = 0
            n = str(n)
            num = str(num)
            correct = ['X']*4
            for i in range(0, 4):
                if n[i] == num[i]:
                    count += 1
                    correct[i] = n[i]
                else:
                    continue
            if count < 4 and count != 0:
                print("Not quite the number. But you did get ", count, " digit(s) correct!")
                print("Also these numbers in your input were correct: ", correct)

                n = int(input("Enter a 4 digit number: "))
            elif count == 0:
                print("None of the numbers in your input were correct.")
                n = int(input("Enter a 4 digit number: "))
            elif count == 4:
                print("You've become a Mastermind!")
                break
        print("It took you ", tries, " tries to get the correct number.")