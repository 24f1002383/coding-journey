ORDINALS = [
    None, "first", "second", "third", "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth",
]

GIFTS = [
    None,
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
]

def verse(day):
    gifts = [GIFTS[n] for n in range(day, 0, -1)]
    if day > 1:
        gifts[-1] = "and " + gifts[-1]
    return f"On the {ORDINALS[day]} day of Christmas my true love gave to me: " + ", ".join(gifts) + ".\n"


def verses(start, end):
    return "\n".join(verse(day) for day in range(start, end + 1))


def recite(start_verse, end_verse):
    return [verse(day).rstrip("\n") for day in range(start_verse, end_verse + 1)]