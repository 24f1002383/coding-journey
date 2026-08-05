def append(list1, list2):
    return list1 + list2

def concat(lists):
    result = []
    for l in lists:
        result += l
    return result

def filter(function, list):
    return [x for x in list if function(x)]

def length(list):
    return len(list)

def map(function, list):
    return [function(x) for x in list]

def foldl(function, list, initial):
    for x in list:
        initial = function(initial, x)
    return initial

def foldr(function, list1, initial):
    accumulator = initial
    for x in reverse(list1):
        accumulator = function(accumulator, x)
    return accumulator

def reverse(list):
    return list[::-1]