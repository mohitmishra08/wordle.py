mport random

words = [
"apple", "grape", "mango", "peach",
"berry", "lemon", "chair", "plant",
"house", "table"
]

secret = random.choice(words)

print("=" * 30)
print(" WORDLE GAME")
print("=" * 30)
print("Guess the 5-letter word.")
print("You have 6 attempts.")
print("🟩 = Correct")
print("🟨 = Wrong position")
print("⬜ = Not in word")

attempt = 1

while attempt <= 6:

guess = input(f"\nAttempt {attempt}: ").lower()

if len(guess) != 5:
print("Enter exactly 5 letters.")
continue

result = ""

for i in range(5):

if guess[i] == secret[i]:
result += "🟩"

elif guess[i] in secret:
result += "🟨"

else:
result += "⬜"

print(result)

if guess == secret:
print("Congratulations!")
print("You guessed the word.")
break

attempt += 1

if guess != secret:
print("\nGame Over!")
print("Correct word:", secret)

print("\nThanks for playing!")
