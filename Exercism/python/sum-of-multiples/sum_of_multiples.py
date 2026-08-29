from itertools import combinations
from math import lcm

def sum_of_multiples(limit, multiples):
    """
    Returns the sum of all numbers in [1, limit-1] that are divisible
    by at least one number in `multiples`, using inclusion-exclusion.
    
    Time:  O(2^k) where k = number of distinct positive divisors (k is usually small)
    Space: O(1) extra (no set of numbers is built)
    """
    def sum_of_multiples_of_n(n, limit):
        # Sum of multiples of n that are < limit: n + 2n + ... + mn
        m = (limit - 1) // n
        return n * m * (m + 1) // 2

    # Filter to distinct positive divisors only
    divisors = set(d for d in multiples if d > 0)
    if not divisors:
        return 0

    divisors = list(divisors)
    n = len(divisors)
    total = 0

    # Inclusion-exclusion over all non-empty subsets
    for r in range(1, n + 1):
        sign = 1 if r % 2 == 1 else -1
        for combo in combinations(divisors, r):
            l = 1
            for d in combo:
                l = lcm(l, d)
                if l >= limit:
                    break
            if l < limit:
                total += sign * sum_of_multiples_of_n(l, limit)
    return total