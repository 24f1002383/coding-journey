def label(colors):
    
    COLORS = ["black", "brown", "red", "orange", "yellow","green", "blue", "violet", "grey", "white"]

    first = COLORS.index(colors[0])
    second = COLORS.index(colors[1])
    multiplier = COLORS.index(colors[2])

    value = (first * 10 + second) * (10 ** multiplier)

    if value >= 1_000_000_000 and value % 1_000_000_000 == 0:
        return f"{value // 1_000_000_000} gigaohms"
    elif value >= 1_000_000 and value % 1_000_000 == 0:
        return f"{value // 1_000_000} megaohms"
    elif value >= 1_000 and value % 1_000 == 0:
        return f"{value // 1_000} kiloohms"
    else:
        return f"{value} ohms"