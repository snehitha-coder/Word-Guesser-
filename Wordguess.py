import random
import words as w 

# Start of the game
print("Welcome to the Word Guess Game with Hints!")

# Choose level
print("\nChoose a level:")
print(" Easy (8 attempts)")
print(" Medium (5 attempts)")
print(" Hard (4 attempts)")

while True:
    level = input("Enter easy,medium,hard:")
    if level in ["easy", "medium", "hard"]:
        break
    print("Invalid choice. Please enter easy, medium, or hard.")

# Pick word and attempts based on level
if level == "easy":
    word, hint = random.choice(list(w.easy_words.items()))
    attempts = 8
elif level == "medium":
    word, hint = random.choice(list(w.medium_words.items()))
    attempts = 5
else:
    word, hint = random.choice(list(w.hard_words.items()))
    attempts = 4

guessed_letters = []

print("\nHint:", hint)
print("_ " * len(word))

# Game loop
while attempts > 0:
    guess = input("\nGuess a letter : ").lower()

    if len(guess) != 1 :
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        attempts -= 1
        print(f"Wrong. Attempts left: {attempts}")

    # Show current state of the word
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    print("Word:", display.strip())

    # Check win
    if all(letter in guessed_letters for letter in word):
        print(f"\n🎉 You guessed the word: {word}!")
        break
else:
    print(f"\n 😞 Out of attempts! The word was: {word}.")

