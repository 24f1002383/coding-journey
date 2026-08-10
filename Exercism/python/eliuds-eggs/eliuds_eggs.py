def egg_count(display_value):
    count = 0
    
    while display_value:
        display_value &= display_value - 1  # clear the lowest set bit
        count += 1
    return count