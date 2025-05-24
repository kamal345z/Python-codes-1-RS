dict={
    'a': [1, 2, 3],
    'b': [3, 4, 5],
    'c': [5, 6]
}
used = set()

for key in dict:
    uni_val = []
    for value in dict[key]:
        if value not in used:
            uni_val.append(value)
            used.add(value)
    dict[key] = uni_val

print("Dictionary after removing duplicates across values:")
print(dict)