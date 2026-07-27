def triplets_with_sum(number):
    result = []
    for a in range(1, number // 3 + 1):
        x = 2 * (number - a)
        y = number * (number - 2 * a)
        if x <= 0 or y <= 0 or y % x != 0:
            continue
        b = y // x
        c = number - a - b
        if a < b < c:
            result.append([a, b, c])
            
    return result