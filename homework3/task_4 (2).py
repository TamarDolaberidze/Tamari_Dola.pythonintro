from random import randint

list_1 = ["clubs  (♣)", "diamonds (♦)", "hearts (♥)", "spades (♠)"]
list_2 = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

random_element_1 = list_1 [randint(0, 3)]
random_element_2 = list_2 [randint(0, 12)]

print (random_element_1, random_element_2) 
