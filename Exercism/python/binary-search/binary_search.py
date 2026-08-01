def find(search_list, value):
    right,left = 0,len(search_list)-1
    while right <= left:
        mid = (right + left)//2
        if search_list[mid]==value:
            return mid
        elif search_list[mid]<value:
            right = mid + 1
        else:
            left = mid - 1
    raise ValueError("value not in array")