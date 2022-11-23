# Variables
secret_word = "tiger"
guessed_word = ""
guess_limit = 3
guess_count = 2
out_of_guesses = False

# Print hint
print("HINT: I'm an animal which is orange")

# Condition to check if user has guessed the correct word and he still has number of guesses left
while secret_word != guessed_word.lower() and not (out_of_guesses):
    if guess_count < guess_limit:
        guessed_word = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

# Check whether the user has guessed the correct word or not
if out_of_guesses:
    print("You Lost")
else:
    print("You win")
