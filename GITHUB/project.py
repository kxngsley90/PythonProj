import random
num = random.randint(0,20)
pick_num = int(input('pick a random number: '))
while num != pick_num:
    if pick_num < num:
        print('Your input is low')
        pick_num = int(input('Have another go: '))
    elif pick_num > num:
        print('Your input is high')
        pick_num = int(input('Oya try again: '))
    elif pick_num == num / 2:
        print('You are guessed half of the number')
        pick_num = int(input('you should get it now: '))     
    else:
        break
    print('That is correct')


