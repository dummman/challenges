from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        dic = f.read().splitlines()
    #print([res for res in dic if '-' in res])
    return dic

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for l in word.upper():
        try:
            score += LETTER_SCORES[l]
        except KeyError:
            continue
    return score

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(words, key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate
