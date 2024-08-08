data = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def sum_lengths_and_numbers(item):
    total = 0

    if isinstance(item, (int, float)):
        total += item
    elif isinstance(item, str):
        total += len(item)
    elif isinstance(item, (list, tuple, set)):
        for element in item:
            total += sum_lengths_and_numbers(element)
    elif isinstance(item, dict):
        for key, value in item.items():
            total += sum_lengths_and_numbers(key)
            total += sum_lengths_and_numbers(value)

    return total

result = sum_lengths_and_numbers(data)
print(result)