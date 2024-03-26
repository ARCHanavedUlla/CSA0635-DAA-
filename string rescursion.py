def copy_string(source, destination, index=0):
    if index == len(source):
        return destination
    else:
        destination += source[index]
        return copy_string(source, destination, index + 1)

source_str = "Hello, World!"
destination_str = ""
result = copy_string(source_str, destination_str)
print("Copied String:", result)
