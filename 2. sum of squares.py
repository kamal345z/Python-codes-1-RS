def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

def print_square_sums(n):
    print(f"Sum of squares from 1 to {n}:")
    for i in range(1, n + 1):
        print(f"i = {i}: {sum_of_squares(i)}")

# Input from user
try:
    n = int(input("Enter a natural number (n ≥ 1): "))
    if n < 1:
        print("Please enter a number greater than or equal to 1.")
    else:
        print_square_sums(n)
except ValueError:
    print("Invalid input. Please enter a natural number.")