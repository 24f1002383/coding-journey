def flatten(iterable):
    result = []
    for x in iterable:
        if x is None:
            continue
        if isinstance(x, list):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result