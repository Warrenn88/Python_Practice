import random
hand = ("rock", "paper", "scissors")
comp_hand = random.choice(hand)
player_hand = input("Rock, Paper, or Scissors?")
if player_hand.lower() == comp_hand:
    print(f"Draw! We both had {comp_hand}!")
elif player_hand.lower() == "rock" and comp_hand == "scissors":
    print(f"You win! I had {comp_hand} and you had {player_hand}!")
elif player_hand.lower() == "paper" and comp_hand == "rock":
    print(f"You win! I had {comp_hand} and you had {player_hand}!")
elif player_hand.lower() == "scissors" and comp_hand == "paper":
    print(f"You win! I had {comp_hand} and you had {player_hand}!")
elif player_hand.lower() == "paper" and comp_hand == "scissors":
    print(f"You lose! I had {comp_hand} and you had {player_hand}!")
elif player_hand.lower() == "scissors" and comp_hand == "rock":
    print(f"You lose! I had {comp_hand} and you had {player_hand}!")
elif player_hand.lower() == "rock" and comp_hand == "paper":
    print(f"You lose! I had {comp_hand} and you had {player_hand}!")
