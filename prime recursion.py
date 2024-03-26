def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

def generate_primes_recursive(limit, current=2):
    if current <= limit:
        if is_prime(current):
            print(current, end=" ")
        generate_primes_recursive(limit, current + 1)

# Example usage
limit = int(input("Enter the limit: "))
print("Prime numbers up to", limit, "are:")
generate_primes_recursive(limit)
