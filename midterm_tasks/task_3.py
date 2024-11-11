import random 

def play(r, p, s):
    list_choices = ["R", "P", "S"]
    return random.choice(list_choices)

def determine_winner(player_input, computer_rand):
    if player_input == computer_rand:
        return "game is even"
    else:
        if (player_input == "R" and computer_rand == "S") or (player_input == "S" and computer_rand == "P") or (player_input == "P" and computer_rand == "R"):
            return "Player is a winner"
        elif (player_input == "S" and computer_rand == "R") or (player_input == "P" and computer_rand == "S") or (player_input == "R" and computer_rand == "P"): 
            return "Computer is a winner"

def main():
    player_input = input("Enter a choice 'R' 'S' or 'P': ")
    result = determine_winner(player_input, play("R", "P", "S"))
    print(result)

if __name__ == "__main__":
    main()
