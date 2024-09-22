import random 

players_num = int (input ("please enter  a players number - "))

for i in range(players_num):
    dice_num_1 = random.randint (1, 6)
    dice_num_2 = random.randint (1, 6)
    print (dice_num_1, dice_num_2)