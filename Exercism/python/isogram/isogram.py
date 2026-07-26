def is_isogram(string):
    x = set()
    for ch in string.lower():
        if ch.isalpha():
            if ch in x:
                return False
            x.add(ch)
    return True