def generate_pascal_triangle(num_rows):
    triangle = []

    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))

# Example usage
num_rows = int(input("Enter the number of rows for Pascal's Triangle: "))
pascal_triangle = generate_pascal_triangle(num_rows)
print("Pascal's Triangle:")
print_pascal_triangle(pascal_triangle)
