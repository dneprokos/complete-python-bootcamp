# Write a function that computes the volume of a sphere given its radius

def vol(rad):
    return (4/3) * 3.14 * (rad ** 3)


print(vol(2))  # 33.49333333333333

# Write a function which checks whether a number in a given range (inclusive)


def ran_check(num, low, high):
    return num in range(low, high + 1)


# Calculate number of up and low chars

def up_low(s):
    lower_case = 0
    upper_case = 0

    for char in s:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
        else:
            pass

    print(f"Original string: {s}")
    print(f"Lowercase count: {lower_case}")
    print(f"Uppercase count: {upper_case}")


def up_low_with_dict(s):
    d = {'upper': 0, 'lower': 0}

    for char in s:
        if char.isupper():
            d['upper'] += 1
        elif char.islower():
            d['lower'] += 1
        else:
            pass

    print(f"Original string: {s}")
    print(f"Lowercase count: {d['lower']}")
    print(f"Uppercase count: {d['upper']}")


# Write a function that takes a list and returns unique list of the elements


def unique_list(lst):
    return list(set(lst))


print(unique_list([1, 1, 1, 2, 3, 2, 4, 5, 1]))  # [1, 2, 3, 4, 5]

# Write a function to multiply all numbers


def multiply(numbers):
    total = 1
    for num in numbers:
        total = total * num

    return total


# Python Palindrome function


def palindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1]

