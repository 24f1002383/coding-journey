def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1:
        return "deficient"

    total = 1  # 1 is a proper divisor of every number > 1

    i = 2
    while i * i <= number:
        if number % i == 0:
            total += i
            if i != number // i:  # Avoid adding the square root twice
                total += number // i
        i += 1

    if total == number:
        return "perfect"
    elif total > number:
        return "abundant"
    else:
        return "deficient"