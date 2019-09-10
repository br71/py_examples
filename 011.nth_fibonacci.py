

# Recursive solution
# O(n^2) time | O(n) space
def get_nth_fib1(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return get_nth_fib1(n - 1) + get_nth_fib1(n - 2)


# Recursive solution with dictionary
# O(n) time | O(n) space_
def get_nth_fib2(n, mem={1: 0, 2: 1}):
    if n in mem:
        return mem[n]
    else:
        mem[n] = get_nth_fib2(n - 1, mem) + get_nth_fib2(n - 2, mem)
        return mem[n]


# Iterative solution
# O(n) time | O(1) space_
def get_nth_fib3(n):
    last_two = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    return last_two[1] if n > 1 else last_two[0]





