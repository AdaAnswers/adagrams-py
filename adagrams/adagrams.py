from adagrams.hand import Hand

class Adagrams:
    def __init__(self, letter_pool, letter_values):
        self.letter_values = letter_values
        self.hand = Hand(letter_pool)
        self.word_list = []

    def score_word(self, word):
        word = word.upper()
        score = 0
        for letter in word:
            score += self.letter_values[letter.upper()]

        if len(word) > 6 and len(word) < 11:
            score += 8

        return score

    def add_valid_word_to_list(self, word):
        if self.hand.uses_available_letters(word):
            self.word_list.append(word)
            print(f"Nice {len(word)} letter word!")
        else:
            print("You can't make that word")


    def get_highest_word_score(self):
        if not self.word_list:
            return None
            
        highest = (self.word_list[0],0)
        for word in self.word_list:
            score = self.score_word(word)
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