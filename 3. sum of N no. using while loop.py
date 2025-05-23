
N = int(input("Enter how many numbers you want to sum: "))

# Initialize variables
count = 0
total_sum = 0

# Use while loop to get N numbers and compute the sum
while count < N:
    num = float(input(f"Enter number {count + 1}: "))
    total_sum += num
    count += 1

# Print the result
print("The total sum is:", total_sum)