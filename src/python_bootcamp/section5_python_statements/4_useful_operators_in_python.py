# -------------Range
for num in range(10):  # Will generate numbers from 0 to 9 (10 is not included)
    print(num)

for num in range(5, 10):  # Will generate number from 5 to 9
    print(num)

for num in range(0, 10, 2):  # Will generate number from 0 to 9 with step 2
    print(num)
    """
    0
    2
    4
    6
    8
    """

print(list(range(11)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# -------------Enumeration
index_count = 0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count += 1
    """
    a
    b
    c
    d
    e
    """

for item in enumerate(word):
    print(item)
    """
    (0, 'a')
    (1, 'b')
    (2, 'c')
    (3, 'd')
    (4, 'e')
    """

for index, letter in enumerate(word):
    print(letter)
    """
    a
    b
    c
    d
    e
    """

# -------------ZIP
numeric_list = [1, 2, 3, 4, 5]
string_list = ['a', 'b', 'c']

for item in zip(numeric_list, string_list):
    print(item)
    """
    (1, 'a')
    (2, 'b')
    (3, 'c')
    """

print('a' in 'a world')  # TRUE

print('mykey' in {'mykey': 345}) # TRUE

print(min([10, 20, 30]))  # 10
print(max([10, 20, 30]))  # 30

from random import shuffle  # Import should be on top. This is just an example

ordered_list = [1, 2, 3, 4, 5, 6]
shuffle(ordered_list)
print(ordered_list)  # It was randomly shuffled

from random import randint
print(f"This is random number: {randint(0, 10)}")

result = input('What is your name?')
print(result)
