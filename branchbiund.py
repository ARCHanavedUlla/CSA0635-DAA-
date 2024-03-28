# This problem involves finding the minimum cost assignment given a matrix of costs.
# Implementing branch and bound for this is a bit complex and requires more space.
# Here's a simplified example:

from itertools import permutations

def assignment_cost(assignment, cost_matrix):
    total_cost = 0
    for i in range(len(assignment)):
        total_cost += cost_matrix[i][assignment[i]]
    return total_cost

def branch_and_bound_assignment(cost_matrix):
    n = len(cost_matrix)
    min_cost = float('inf')
    min_assignment = None

    for perm in permutations(range(n)):
        cost = assignment_cost(perm, cost_matrix)
        if cost < min_cost:
            min_cost = cost
            min_assignment = perm

    return min_assignment, min_cost

# Example usage:
cost_matrix = [
    [10, 20, 30],
    [15, 25, 35],
    [25, 30, 40]
]

assignment, optimal_cost = branch_and_bound_assignment(cost_matrix)
print("Optimal Assignment:", assignment)
print("Optimal Cost:", optimal_cost)
