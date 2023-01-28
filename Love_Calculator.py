print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


lower_name1 = name1.lower()
lower_name2 = name2.lower()

T_count1 = lower_name1.count('t')
T_count2 = lower_name2.count('t')
R_count1 = lower_name1.count('r')
R_count2 = lower_name2.count('r')
U_count1 = lower_name1.count('u')
U_count2 = lower_name2.count('u')
E_count1 = lower_name1.count('e')
E_count2 = lower_name2.count('e')

L_count1 = lower_name1.count('l')
L_count2 = lower_name2.count('l')
O_count1 = lower_name1.count('o')
O_count2 = lower_name2.count('o')
V_count1 = lower_name1.count('v')
V_count2 = lower_name2.count('v')

score_TRUE = T_count1 + T_count2 + R_count1 + R_count2 + U_count1 + U_count2 + E_count1 + E_count2
score_LOVE = L_count1 + L_count2 + O_count1 + O_count2 + V_count1 + V_count2 + E_count1 + E_count2
score = int(str(score_TRUE) + str(score_LOVE))

if score <10 or score > 90:
    print("Your score is " + str(score) + ", you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print("Your score is " + str(score) + ", you are alright together.")
else:
    print("Your score is " + str(score) + ".")

