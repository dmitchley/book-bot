list_of_dicts = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

for item in list_of_dicts:
    for key, value in item.items():
        print(f"{key}: {value}")
    print("---")  # Just to separate each dictionary's output
