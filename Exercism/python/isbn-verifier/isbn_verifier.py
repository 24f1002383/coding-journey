def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False
    Sum = 0
    for i, ch in enumerate(isbn):
        if ch == "X":
            if i != 9:
                return False
            ch = 10
        elif ch.isdigit():
            ch = int(ch)
        else:
            return False
        Sum += ch * (10 - i)
    return Sum % 11 == 0