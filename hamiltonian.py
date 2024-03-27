def is_valid(v, graph, path, pos):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def hamiltonian_circuit_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False
    for v in range(1, len(graph)):
        if is_valid(v, graph, path, pos):
            path[pos] = v
            if hamiltonian_circuit_util(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False

def hamiltonian_circuit(graph):
    path = [-1] * len(graph)
    path[0] = 0
    if not hamiltonian_circuit_util(graph, path, 1):
        print("Solution does not exist.")
        return False
    print("Solution exists. Hamiltonian Circuit:")
    print(path + [path[0]])

graph = [[0, 1, 0, 1, 0],
         [1, 0, 1, 1, 1],
         [0, 1, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [0, 1, 1, 1, 0]]
hamiltonian_circuit(graph)
