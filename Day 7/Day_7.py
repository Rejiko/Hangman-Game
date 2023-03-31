import random
import hangmanart as ha
import hangmanwords as hw

chosen_word = random.choice(hw.words)

lives = 6
display = []
end_of_game = False

for _ in range(len(chosen_word)):
    display += "_"

print(ha.hangmanlogo)

#while the player still has lives, continue the game
while not end_of_game:


    #ask the player to guess a letter
    guess = input("Guess a letter: ").lower()


    if guess not in chosen_word:
        lives -=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True

    #Loop through each letter in the chosen word
    if guess in display:
        print(f"You have already guessed {guess}")
    else:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess

    #Print the display with the updated letter
    print(f"{' '.join(display)}")

    #Check if there are any underscores left in the display
    if "_" not in display:
        end_of_game = True
        print("You win")

    #Print the stage based on the number of lives left
    print(ha.stages[lives])

