str=input("Enter a string:")
freq = {}
for char in str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print("Character frequencies:")
for char, freq in freq.items():
    print(f"'{char}': {freq}")