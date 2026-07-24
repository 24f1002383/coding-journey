def is_armstrong_number(number):
    nums = str(number)
    return number == sum(int(n) ** len(nums) for n in nums)