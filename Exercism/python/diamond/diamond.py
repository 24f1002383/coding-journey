def rows(letter):
    n = ord(letter) - ord('A')
    width = 2 * n + 1
    top = []
    for i in range(n + 1):
        ch = chr(ord('A') + i)
        middle = ch if i == 0 else ch + ' ' * (2 * i - 1) + ch
        top.append(middle.center(width))

    return top + top[-2::-1]   # mirror without recomputation