import math
def triplets_with_sum(number):

    if number <= 0 or number % 2 != 0:
        return []

    result = []
    m = 2
    while 2 * m * (m + 1) <= number:
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                perimeter_unit = 2 * m * (m + n)
                if number % perimeter_unit == 0:
                    k = number // perimeter_unit
                    a = k * (m * m - n * n)
                    b = k * (2 * m * n)
                    c = k * (m * m + n * n)
                    if a > b:
                        a, b = b, a
                    result.append([a, b, c])
        m += 1
    return result