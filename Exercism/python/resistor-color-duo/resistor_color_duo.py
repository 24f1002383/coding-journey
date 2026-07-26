def value(colors):
    
    COLORS = ["black", "brown", "red", "orange", "yellow","green", "blue", "violet", "grey", "white"]
    first = COLORS.index(colors[0])
    second = COLORS.index(colors[1])

    return first * 10 + second
