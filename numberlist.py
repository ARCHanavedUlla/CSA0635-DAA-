def insert_number(num, lst, index):
    lst.insert(index, num)
    return lst

# Example usage:
num = 100
lst = [1, 2, 3, 4, 5]
index = 2
result = insert_number(num, lst, index)
print("List after inserting number:", result)
