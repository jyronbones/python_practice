import random
player_choice = ""
rock = 0
rock_ascii_art = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = 1
paper_ascii_art = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = 2
scissors_ascii_art = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
continue_playing = True
while continue_playing:
    while True:
        player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:")
        if player_choice == "0" or player_choice == "1" or player_choice == "2":
            break
        else:
            print("Not a valid selection, please try again...")
            player_choice = ""

    player_choice = int(player_choice)
    computer_choice = random.randint(0, 2)
    player_pick = ''
    computer_pick = ''
    if player_choice == rock:
        player_pick = rock_ascii_art
    elif player_choice == paper:
        player_pick = paper_ascii_art
    else:
        player_pick = scissors_ascii_art

    if computer_choice == rock:
        computer_pick = rock_ascii_art
    elif computer_choice == paper:
        computer_pick = paper_ascii_art
    else:
        computer_pick = scissors_ascii_art

    print(f"Player:\n{player_pick}\nComputer:\n{computer_pick}")
    if player_choice == rock and computer_choice == paper:
        print("You lose, the computer beat your rock with paper")
    elif player_choice == rock and computer_choice == scissors:
        print("You WIN, you beat the computer's scissors with rock")
    elif player_choice == rock and computer_choice == rock:
        print("DRAW, the computer also threw down rock")
    elif player_choice == paper and computer_choice == rock:
        print("You WIN, your paper beat the computer's rock")
    elif player_choice == paper and computer_choice == paper:
        print("DRAW, the computer also picked paper")
    elif player_choice == paper and computer_choice == scissors:
        print("You lose, the computer beat your paper with scissors")
    elif player_choice == scissors and computer_choice == rock:
        print("You lose, the computer beat your rock with scissors")
    elif player_choice == scissors and computer_choice == paper:
        print("You WIN, your scissors beat the computer's rock")
    elif player_choice == scissors and computer_choice == scissors:
        print("DRAW, you BOTH picked scissors")

    while True:
        continue_choice = input("Would you like to continue playing? yes or no:").lower()
        if continue_choice == "yes" or continue_choice == "no":
            if continue_choice == "yes":
                continue_playing = True
            else:
                continue_playing = False
            break
        else:
            print("Not a valid option, try again...")
            continue_choice = ""

print("Thanks for playing, good-bye!")
