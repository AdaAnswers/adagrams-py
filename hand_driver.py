from adagrams.hand import Hand

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
play = True

hand = Hand(LETTER_POOL)

print("Welcome to Adagrams!")
print("Let's draw some letters!")
print(f"Here is the letter bank: {hand.letter_bank}")

while play:
    word = input("Give me a word with the letters: ")
    if hand.uses_available_letters(word):
        print(f"Nice {len(word)} letter word!")
    else:
        print("You can't make that word")

    another = input("Would you like to input another word (W), draw a new hand (H), or quit (Q)")

    if another.upper() == "H":
        hand = Hand(LETTER_POOL)
        print(f"Here is the letter bank: {hand.letter_bank}")
    elif another.upper() == "Q":
        play = False
    elif another.upper() == "W":
        pass
    else:
        print("Invalid Choice, Make another word")




