def sum_of_subsets_util(arr, n, sum, subset, index):
    if sum == 0:
        print(subset)
        return
    if sum < 0 or index == n:
        return
    subset.append(arr[index])
    sum_of_subsets_util(arr, n, sum - arr[index], subset, index + 1)
    subset.pop()
    sum_of_subsets_util(arr, n, sum, subset, index + 1)

def sum_of_subsets(arr, n, target_sum):
    subset = []
    sum_of_subsets_util(arr, n, target_sum, subset, 0)

arr = [int(x) for x in input("Enter the array elements separated by space: ").split()]
target_sum = int(input("Enter the target sum: "))
sum_of_subsets(arr, len(arr), target_sum)
