def find_factors(n, divisor=1, factors=None):
    if factors is None:
        factors = []
    if divisor > n:
        return factors
    if n % divisor == 0:
        factors.append(divisor)
    return find_factors(n, divisor + 1, factors)

# Example usage:
n = 20
print(f"Factors of {n}: {find_factors(n)}")
