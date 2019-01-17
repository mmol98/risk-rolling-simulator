from random import randint

dice = input('how many dices are you throwing?')
for x in range(int(dice)):
    print(x, randint(1, 6))



