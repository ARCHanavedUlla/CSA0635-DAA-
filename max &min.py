def find_max_min(arr, low, high):
    if low == high:  # Only one element in the list
        return arr[low], arr[low]

    elif high - low == 1:  # Only two elements in the list
        return (arr[low], arr[high]) if arr[low] < arr[high] else (arr[high], arr[low])

    else:
        mid = (low + high) // 2
        max_left, min_left = find_max_min(arr, low, mid)  # Divide and conquer left half
        max_right, min_right = find_max_min(arr, mid + 1, high)  # Divide and conquer right half

        return max(max_left, max_right), min(min_left, min_right)


# Example usage
arr = [3, 7, 2, 11, 6, 1, 9, 4]
max_val, min_val = find_max_min(arr, 0, len(arr) - 1)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
