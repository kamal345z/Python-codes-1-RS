data = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)

col = zip(*data)
avg = [sum(col) / len(col) for col in col]

print(f" The Average value of the numbers of the said tuple of tuples:{avg}")