import random

print("Let's Start the Game!!!")

my_word_list = [
    ["table", "furniture"],
    ["gelpen", "stationary"],
    ["mobile", "electronic device"],
    ["tree", "nature"],
    ["funkopop", "collectible toy item"]
]

hangman = [
    "Head",
    "Left Arm",
    "Right Arm",
    "Body",
    "Left Leg",
    "Right Leg",
]

rope_stand = []

# Extract items from the first column and their corresponding types
word_to_type = {item[0]: item[1] for item in my_word_list}

# Generate a random word from the first column items
random_word = random.choice(list(word_to_type.keys()))

random_word_length = len(random_word)

# Access the appropriate type for the randomly generated word
word_type = word_to_type[random_word]

# print(f"Random Word: {random_word}")
# print(f"Type: {word_type}")

# Access individual letters from the random word
letters = [letter for letter in random_word]

print("Let's Start Hangman Game!")

print("Now guess the word!")
print(f"The word has {len(random_word)} letters and is a {word_type}")

guess_letter = []

# Track if the user has guessed all letters
correct_guesses = set()

while len(hangman) > 0 and set(letters) != correct_guesses:
    print("")
    user_input = input("Enter your guess for a letter: ").lower()

    if user_input in letters:
        print("Nice One! You guessed a letter correctly!")
        correct_guesses.add(user_input)
        guess_letter = list(correct_guesses)
        guess_letters_sorted = sorted(correct_guesses)
        print("Guessed Letters: ", guess_letters_sorted)
    else:
        print("Wrong Guess!")
        if hangman:
            rope_stand.append(hangman.pop(0))  # Append the next hangman stage
        print("Hangman Status: ", rope_stand)
        print("Remaining Hangman Stages: ", hangman)

        # Check if the game is over
        if len(hangman) == 0:
            print("Game Over!")
            break  # Exit the loop as the game is over

# Check if the user has guessed all letters
if set(letters) == correct_guesses:
    print("Congratulations! You guessed the word correctly!")
else:
    print("The word was: ", random_word)





