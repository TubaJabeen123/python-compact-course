# Task 4: list of strings -> list of lists, using map()

def strings_to_lists(strings):
    return list(map(list, strings))


strings = ["hello", "world", "python"]

result = strings_to_lists(strings)

print("Original list:")
print(strings)

print("\nList of lists:")
print(result)