l=['a','b','c']
d={'a':1,'b':2,'d':3}

A = input("Enter the key to check: ")

if A in l and A in d:
    print(f"The value of '{A}' from the dictionary is: {dict[A]}")
else:
    print(f"The key '{A}' isn't present in  the list and the dictionary.")