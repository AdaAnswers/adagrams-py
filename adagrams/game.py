import random

def draw_letters():
    # Keep data inside function since it's only used here
    distribution = {'A': 9, 'B': 2, 'O': 8, 'C': 2, 'P': 2, 
                    'D': 4, 'Q': 1, 'E': 12, 'R': 6, 'F': 2, 
                    'S': 4, 'G': 3, 'T': 6, 'H': 2, 'U': 4, 
                    'I': 9, 'V': 2, 'J': 1, 'W': 2, 'K': 1, 
                    'X': 1, 'L': 4, 'Y': 2, 'M': 2, 'Z': 1}
    pool = []
    for letter in distribution:
        pool.extend([letter for _ in range(distribution[letter])])
    
    # Using random.sample:
    # hand = random.sample(pool, 10)

    # manual version:
    hand = []
    for _ in range(10):
        # randint is inclusive
        index = random.randint(0, len(pool) - 1)
        letter = pool[index]
        hand.append(letter)
        pool.remove(letter)

    return hand

def uses_available_letters(word, letter_bank):
    word = word.upper()

    letter_counts = {}
    for letter in letter_bank:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    for letter in word:
        if letter in letter_counts and letter_counts[letter] > 0:
            letter_counts[letter] -= 1
        else:
            return False
        
    return True

def score_word(word):
    scores = {'A': 1, 'B': 3, 'O': 1, 'C': 3, 'P': 3, 
                'D': 2, 'Q': 10, 'E': 1, 'R': 1, 'F': 4, 
                'S': 1, 'G': 2, 'T': 1, 'H': 4, 'U': 1, 
                'I': 1, 'V': 4, 'J': 8, 'W': 4, 'K': 5, 
                'X': 8, 'L': 1, 'Y': 4, 'M': 3, 'Z': 10}
    
    word = word.upper()
    score = 0
    for letter in word:
        score += scores[letter]

    if len(word) >= 7:
        score += 8

    return score

def get_highest_word_score(word_list):
    if not word_list:
        return None
    
    highest = (word_list[0],0)
    for word in word_list:
        score = score_word(word)
        if score > highest[1]:
            highest = (word, score)
            
        elif score == highest[1]:
            if len(highest[0]) == 10:
                continue
            elif len(word) == 10 and len(highest[0]) != 10:
                highest = (word, score)
            elif len(word) < len(highest[0]):
                highest = (word, score)

    return highest
