def square_root(number):
    low = 0
    high = number
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            low = mid + 1
        else:
            high = mid - 1