def merge_dicts(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    merged = d1.copy()
    for key, val in d2.items():
        if key in merged:
            merged[key] += val
        else:
            merged[key] = val

    return merged

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = merge_dicts(d1, d2)
print(merged)
# Expected Output: {'a': 1, 'b': 5, 'c': 4}
