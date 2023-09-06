print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

way = input("Wich way do you choose, left or right?\n")
way = way.lower()
num_way_l = way.count("left")
num_way_r = way.count("right")

if num_way_l == 1:
    swim = input("\nCongratulations you made the right decision!\n"
                 "You arrived at a river do you want to swim or do you want to wait?\n")
    swim = swim.lower()
    num_swim_s = swim.count("swim")
    num_swim_w = swim.count("wait")

    if num_swim_s == 1:
        print("\nYou got attacked by a trout\nGame Over!")
    elif num_swim_w == 1:
        door = input("\nWaiting was the right decision now you get to choose a door\n"
                     "wich door do you choose the red, yellow or the blue one?\n")
        door = door.lower()
        num_door_y = door.count("yellow")
        num_door_r = door.count("red")
        num_door_b = door.count("blue")

        if num_door_b == 1:
            print("\nYou got eaten by beasts.\nGame Over!")
        elif num_door_r == 1:
            print("\nYou got burned by fire.\nGame Over!")
        elif num_door_y == 1:
            print("You Win!")
        else:
            print("Game Over!")
    else:
        print("You got attacked by a trout\nGame Over!")
elif num_way_r == 1:
    print("\nYou fell into a hole.\nGame Over!")
else:
    print("\nYou fell into a hole.\nGame Over!")
