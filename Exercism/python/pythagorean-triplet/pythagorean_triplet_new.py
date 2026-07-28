def triplets_with_sum(tripletsum):
    n = tripletsum
    if n % 2 != 0 or n < 12:
        return []

    # step 1: find prime factors of n
    def get_prime_factors(x):
        factors = {}
        d = 2
        while d * d <= x:
            while x % d == 0:
                factors[d] = factors.get(d, 0) + 1
                x = x // d
            d += 1
        if x > 1:
            factors[x] = factors.get(x, 0) + 1
        return factors

    n_factors = get_prime_factors(n)

    # k = n*n // 2, so double every exponent, then remove one factor of 2
    k_factors = {}
    for prime, exp in n_factors.items():
        k_factors[prime] = exp * 2
    k_factors[2] -= 1

    # step 2: build all divisors of k from its prime factors
    divisors = [1]
    for prime, exp in k_factors.items():
        new_divisors = []
        power = 1
        for _ in range(exp + 1):
            for d in divisors:
                new_divisors.append(d * power)
            power *= prime
        divisors = new_divisors

    # step 3: check each divisor as a candidate for y
    k = n * n // 2
    low = n // 2

    triplets = []
    for y in divisors:
        if y <= low:
            continue
        x = k // y
        a = n - x
        b = n - y
        c = n - a - b
        if 0 < a < b < c:
            triplets.append([a, b, c])

    return triplets