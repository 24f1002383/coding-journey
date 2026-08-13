from collections import Counter

def find_anagrams(word, candidates):
    word_lower = word.lower()
    target = Counter(word_lower)

    return [
        c for c in candidates
        if len(c) == len(word)
        and c.lower() != word_lower
        and Counter(c.lower()) == target
    ]