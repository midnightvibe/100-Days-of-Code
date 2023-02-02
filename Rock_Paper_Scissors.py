import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rpc = [rock, paper, scissors]
selection = int(input("What do you choose Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(rpc[selection])

computer_selection = random.randint(0, 2)
print(f"The computer chose: {rpc[computer_selection]}")

if selection == 0 and computer_selection == 1:
    print("You lose")
elif selection == 0 and computer_selection == 2:
    print("You win")
elif selection == 1 and computer_selection == 0:
    print("You win")
elif selection == 1 and computer_selection == 2:
    print("You lose")
elif selection == 2 and computer_selection == 0:
    print("You lose")
elif selection == 2 and computer_selection == 1:
    print("You win")
else:
    print("draw")

