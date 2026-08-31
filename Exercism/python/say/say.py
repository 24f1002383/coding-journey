ONES = ["zero", "one", "two", "three", "four","five", "six", "seven", "eight", "nine","ten", "eleven", "twelve", "thirteen", "fourteen","fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty","fifty", "sixty", "seventy", "eighty", "ninety"]
def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    if number < 20:
        return ONES[number]
    if number < 100:
        return TENS[number // 10] + (
            "-" + ONES[number % 10] if number % 10 else ""
        )
    if number < 1000:
        return (
            ONES[number // 100]
            + " hundred"
            + (" " + say(number % 100) if number % 100 else "")
        )
    if number < 1_000_000:
        return (
            say(number // 1000)
            + " thousand"
            + (" " + say(number % 1000) if number % 1000 else "")
        )
    if number < 1_000_000_000:
        return (
            say(number // 1_000_000)
            + " million"
            + (" " + say(number % 1_000_000) if number % 1_000_000 else "")
        )
    return (
        say(number // 1_000_000_000)
        + " billion"
        + (" " + say(number % 1_000_000_000) if number % 1_000_000_000 else "")
    )