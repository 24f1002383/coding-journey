def commands(binary_str):
    number = int(binary_str, 2)
    result = []
    if number & 1:
        result.append("wink")
    if number & 2:
        result.append("double blink")
    if number & 4:
        result.append("close your eyes")
    if number & 8:
        result.append("jump")
    if number & 16:
        result.reverse()
    return result
