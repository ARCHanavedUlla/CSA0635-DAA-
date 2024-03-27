def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [int(x) for x in input("Enter the array elements separated by space: ").split()]
target = int(input("Enter the target element to search: "))
index = linear_search(arr, target)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found in the array.")
