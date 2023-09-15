import random

class Hand:
    def __init__(self, letter_pool):
        self.letter_bank = self.draw_letters(letter_pool)
        
    def draw_letters(letter_pool):
        pool = []
        for letter in letter_pool:
            pool.extend([letter for _ in range(letter_pool[letter])])
        
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
