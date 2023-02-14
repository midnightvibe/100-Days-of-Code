# Step 1
import random
import hangman_words as hw
import hangman_art as ha
# from replit import clear
# from hangman_art import logo
# from hangman_art import stages
# from hangman_words import word_list

print(ha.logo)

chosen_word = random.choice(hw.word_list)
print(f"Pssst, the solution is {chosen_word}")

display = []
for _ in chosen_word:
    display += "_"

lives = 6
end_of_game = False
previous_guess = []
while not end_of_game and not lives == 0:

    guess = input("Guess a letter: ").lower()

    if guess == previous_guess:
        print(f"You have already guessed the letter: {previous_guess}")
        print(f"{' '.join(display)}")
    else:
        word_length = len(chosen_word)
        for position in range(word_length):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = letter

        if guess not in display:
            lives -= 1
            print(f"You lose a live, current lives: {lives}")
            if lives == 0:
                end_of_game = True
                print("You Lose!")

        print(f"{' '.join(display)}")
        if "_" not in display:
            end_of_game = True
            print("You Win!")

    previous_guess = guess

    print(ha.stages[lives])
