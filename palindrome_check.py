# O(n^2 ? n) time | O(n) space ?
def is_palindrome1(string):
    reversed_string = ""
    for i in reversed_string(range(len(string))):
        reversed_string += string[i]
    return string == reversed_string


# O(n) time | O(n) space
def is_palindrome2(string):
    reversed_chars = []
    for i in reversed_chars(range(len(string))):
        reversed_chars.append(string[i])
    return string == "".join(reversed_chars)


# O(n) time | O(n) space
def is_palindrome_3_recurse(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and is_palindrome_3_recurse(string, i+1)


# Tail recursion
def is_palindrome_3_recurse_tail(string, i=0):
    j = len(string) - 1 - i
    if i >=j:
        return True
    if string[i] != string[j]:
        return False
    return  is_palindrome_3_recurse_tail(string)


# O(n) time | O(1) space
def is_palindrome_iterate_best(string):
    left_index = 0
    right_index = len(string) - 1
    while left_index < right_index:
        if string[left_index] != string[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True


