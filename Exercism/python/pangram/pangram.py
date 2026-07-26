def is_pangram(sentence):

    letters = set()
    for ch in sentence.lower():
        if ch.isalpha():
            letters.add(ch)
    return len(letters) == 26