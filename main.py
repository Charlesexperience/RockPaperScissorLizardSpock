import random
print("""This is a game called Rock Paper Scissors Lizard Spock from th hit TV show, The Big Bang Theory.
The rules are as follows:
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
(and as it always has) Rock crushes Scissors
""")
print("Your goal is to beat me in a best of three.")
choices = ["rock", "paper", "scissors", "lizard", "spock"]
user_score = 0
cpu_score = 0
turn_counter = 1

while turn_counter < 4:
    print(f"Turn number: {turn_counter}")
    user_input = input("Make your choice: ")
    lowered_input = user_input.lower()
    cpu_input = choices[random.randint(0, 4)]
    print(f"Your Choice: {lowered_input}")
    print(f"My Choice: {cpu_input}")
    turn_counter += 1
    if cpu_input == lowered_input:
        print("Draw")
    elif cpu_input == "scissors" and lowered_input == "paper":
        print("Unlucky")
        cpu_score += 1
    elif cpu_input == "paper" and lowered_input == "rock":
        print("Unlucky")
        cpu_score += 1
    elif cpu_input == "rock" and lowered_input == "lizard":
        print("Unlucky")
        cpu_score += 1
    elif cpu_input == "lizard" and lowered_input == "spock":
        print("Unlucky")
        cpu_score += 1
    elif cpu_input == "spock" and lowered_input == "scissors":
        print("Unlucky")
        cpu_score += 1
    elif cpu_input == "scissors" and lowered_input == "lizard":
        print("Unlucky")
        cpu_score += 1
    elif cpu_input == "lizard" and lowered_input == "paper":
        print("Unlucky")
        cpu_score += 1
    elif cpu_input == "paper" and lowered_input == "spock":
        print("Unlucky")
        cpu_score += 1
    elif cpu_input == "spock" and lowered_input == "rock":
        print("Unlucky")
        cpu_score += 1
    elif cpu_input == "rock" and lowered_input == "scissors":
        print("Unlucky")
        cpu_score += 1
    elif lowered_input == "scissors" and cpu_input == "paper":
        print("Unlucky")
        user_score += 1
    elif lowered_input == "paper" and cpu_input == "rock":
        print("Unlucky")
        user_score += 1
    elif lowered_input == "rock" and cpu_input == "lizard":
        print("Unlucky")
        user_score += 1
    elif lowered_input == "lizard" and cpu_input == "spock":
        print("Unlucky")
        user_score += 1
    elif lowered_input == "spock" and cpu_input == "scissors":
        print("Unlucky")
        user_score += 1
    elif lowered_input == "scissors" and cpu_input == "lizard":
        print("Unlucky")
        user_score += 1
    elif lowered_input == "lizard" and cpu_input == "paper":
        print("Unlucky")
        user_score += 1
    elif lowered_input == "paper" and cpu_input == "spock":
        print("Unlucky")
        user_score += 1
    elif lowered_input == "spock" and cpu_input == "rock":
        print("Unlucky")
        user_score += 1
    elif lowered_input == "rock" and cpu_input == "scissors":
        print("Unlucky")
        user_score += 1
    else:
        print("Try again dafty!")
        user_score -= 1



if cpu_score > user_score:
    print("Bad luck sport, you lose")
elif cpu_score < user_score:
    print("Nice one kid, you win")
else:
    print("Guess we both won that one")