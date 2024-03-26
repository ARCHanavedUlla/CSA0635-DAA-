def knapsack_greedy(values, weights, capacity):
    n = len(values)
    # Calculate value to weight ratio
    value_weight_ratio = [(values[i] / weights[i], i) for i in range(n)]
    # Sort items based on value to weight ratio
    value_weight_ratio.sort(reverse=True)
    
    max_value = 0
    knapsack = [0] * n

    for ratio, i in value_weight_ratio:
        if weights[i] <= capacity:
            max_value += values[i]
            capacity -= weights[i]
            knapsack[i] = 1
        else:
            fraction = capacity / weights[i]
            max_value += fraction * values[i]
            knapsack[i] = fraction
            break

    return max_value, knapsack

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, knapsack = knapsack_greedy(values, weights, capacity)
print("Maximum value:", max_value)
print("Knapsack:", knapsack)
