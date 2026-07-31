def is_paired(input_string):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for ch in input_string:
        if ch in pairs:
            stack.append(pairs[ch])      # Push the expected closing bracket
        elif ch in pairs.values():
            if not stack or stack.pop() != ch:
                return False

    return not stack