def min_max_sequence(arr):
    min_seq = min(arr)
    max_seq = max(arr)
    return min_seq, max_seq

# Example usage
numbers = [5, 3, 8, 1, 9, 2]
min_val, max_val = min_max_sequence(numbers)
print("Minimum value sequence:", min_val)
print("Maximum value sequence:", max_val)
