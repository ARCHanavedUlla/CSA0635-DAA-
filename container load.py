def container_loader(weights, capacity):
    weights.sort(reverse=True)
    containers = [[] for _ in range(len(weights))]

    for item in weights:
        found = False
        for container in containers:
            if sum(container) + item <= capacity:
                container.append(item)
                found = True
                break
        if not found:
            containers.append([item])

    return containers

# Example usage:
weights = [5, 7, 10, 3, 2, 8, 15]
capacity = 15
result = container_loader(weights, capacity)
print("Container Loading Result:")
for i, container in enumerate(result):
    print(f"Container {i + 1}: {container}")
