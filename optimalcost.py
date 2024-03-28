def optimal_cost_problem(input_data):
    # Define your dynamic programming table
    dp_table = [[0] * (len(input_data[0])) for _ in range(len(input_data))]

    # Base case
    dp_table[0][0] = input_data[0][0]

    # Fill the dynamic programming table
    for i in range(1, len(input_data)):
        for j in range(len(input_data[0])):
            # Calculate the optimal cost for each cell based on the previous cells
            dp_table[i][j] = input_data[i][j] + min(dp_table[i-1][max(0, j-1):min(len(input_data[0]), j+2)])

    # The optimal cost will be the minimum value in the last row of the dp_table
    optimal_cost = min(dp_table[-1])

    return optimal_cost

# Example usage:
input_data = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10]
]
print("Optimal Cost:", optimal_cost_problem(input_data))
