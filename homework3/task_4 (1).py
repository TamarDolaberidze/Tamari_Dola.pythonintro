from random import randint

card_color = randint (1,4)
card_value = randint (1,13) 

if card_color == 1:
    color = "Clubs (♣)"
elif card_color == 2:
    color = "Diamonds (♦)"
elif card_color == 3:
    color = "Hearts (♥)"
elif card_color == 4:
    color = "Spades (♠)"

if card_value == 1:
    value = "A" 
elif card_value == 2:
    value = "K"
elif card_value == 3:
    value = "Q"
elif card_value == 4:
    value = "J"
elif card_value == 5:
    value = 10
elif card_value == 6:
    value = 9
elif card_value == 7:
    value = 8
elif card_value == 8:
    value = 7
elif card_value == 9:
    value = 6
elif card_value == 10:
    value = 5
elif card_value == 11:
    value = 4
elif card_value == 12:
    value = 3
elif card_value == 13:
    value = 2

print (color, value)





