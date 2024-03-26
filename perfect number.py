def is_perfect_number(num):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

def find_perfect_numbers(limit):
    perfect_numbers = []
    for i in range(1, limit + 1):
        if is_perfect_number(i):
            perfect_numbers.append(i)
    return perfect_numbers

limit = int(input("Enter the limit: "))

perfect_nums = find_perfect_numbers(limit)

if perfect_nums:
    print("Perfect numbers up to", limit, "are:", perfect_nums)
else:
    print("No perfect numbers found up to", limit)
