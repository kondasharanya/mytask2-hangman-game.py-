import random
words = ['python', 'java', 'dbms', 'sql', 'os']
word = random.choice(words)
display = ['_'] * len(word)
lives = 6
game_over = False
print("🎮 Welcome to Hangman Game")
while not game_over:
    print("\nWord:", " ".join(display))
    print("Lives left:", lives)
    guess = input("Enter a letter: ").lower()
    if guess in word:
        print(" Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print(" Wrong!")
        lives -= 1
    if lives == 0:
        print("\n You Lose! Word was:", word)
        game_over = True
    elif "_" not in display:
        print("\n You Win! Word was:", word)
        game_over = True