def sum_of_multiples(limit, multiples):
    total = 0

    for number in range(limit):
        for multiple in multiples:
            if multiple != 0 and number % multiple == 0:
                total += number
                break

    return total