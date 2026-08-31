def abbreviate(words):
    words = words.replace("-", " ").replace("_", " ")
    return "".join(word[0].upper() for word in words.split())