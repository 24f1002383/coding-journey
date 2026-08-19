def factors(value):
    i = 2
    result = []
    while value > 1:
        while value % i == 0:
            result.append(i)
            value //= i
        else:
            i += 1
    return result