a = input("Enter a string: ")
def cat_hat_equal(s):
    words = s.split()
    cat_count = words.count("cat")
    hat_count = words.count("hat")
    return cat_count == hat_count


print(cat_hat_equal(a))