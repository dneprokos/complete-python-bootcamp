my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    print(num)

for num in my_list:
    # Check for even
    if num % 2 == 0:
        print(f"Printing 'even' number: {num}")
    else:
        print(f"Printing 'odd' number: {num}")

# Sum calculation
list_sum = 0

for num in my_list:
    list_sum += num
print(list_sum)  # 55

# For with string
my_string = 'Hello World!'
for letter in my_string:
    print(letter)

# For with tuple
tup = (1, 2, 3)

for item in tup:
    print(item)

# For with array of tuples
array_of_tup = [(1, 2), (3, 4), (5, 6), (7, 8)]

for item in array_of_tup:
    print(item)
    """
    (1, 2)
    (3, 4)
    (5, 6)
    (7, 8)
    """

# Tuple unpacking
for (a, b) in array_of_tup:
    print(a)
    print(b)
    """
    1
    2
    3
    4
    5
    6
    7
    8
    """

# For with dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3}

# iterate through keys
for item in d:
    print(item)
    """
    k1
    k2
    k3
    """

# iterate thought all data
for item in d.items():
    print(item)
    """
    ('k1', 1)
    ('k2', 2)
    ('k3', 3)
    """

# Unpacking
for key, value in d.items():
    print(value)
    """
    1
    2
    3
    """

