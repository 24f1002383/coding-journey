def resistor_label(colors):

    COLOR_VALUES = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9,}

    TOLERANCES = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5,'brown': 1, 'red': 2, 'gold': 5, 'silver': 10,}

    if len(colors) == 1:
        return "0 ohms"

    *value_colors, multiplier_color, tolerance_color = colors

    value = 0
    for color in value_colors:
        value = value * 10 + COLOR_VALUES[color]

    ohms = value * 10 ** COLOR_VALUES[multiplier_color]
    tolerance = TOLERANCES[tolerance_color]

    if ohms >= 1_000_000:
        amount, unit = ohms / 1_000_000, "megaohms"
    elif ohms >= 1_000:
        amount, unit = ohms / 1_000, "kiloohms"
    else:
        amount, unit = ohms, "ohms"
    return f"{amount:g} {unit} ±{tolerance:g}%"