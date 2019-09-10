# O(n) time, | O(d) space | d - dept of recursion
def product_sum(array, multiplier=1):
    msum = 0
    for element in array:
        if type(element) is list:
            # Example of error, infinite recursion
            # Argument for function is in brackets
            msum += product_sum((element, multiplier + 1))
        else:
            msum += element
    return msum * multiplier


a = [1, 2, [3], 4, 5]  # 18
print(product_sum(a))


# O(n) time, | O(d) space | d - dept of recursion
def product_sum2(a, m=1):
    s = 0
    for e in a:
        if type(e) is list:
            # this works
            s += product_sum2(e, m + 1)
        else:
            s += e
    return s * m
