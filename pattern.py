def print_pattern(n):
    if n == 0:
        return
    

    for i in range(1, n + 1):
        print(i, end=" ")
    print()
    

    print_pattern(n - 1)

n = 4


print_pattern(n)
