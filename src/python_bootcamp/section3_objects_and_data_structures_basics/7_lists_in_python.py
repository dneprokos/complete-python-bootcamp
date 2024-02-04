my_list = [1, 2, 3]
my_list2 = ['String', 100, 23.2]

# Length
print(len(my_list))

# Slicing
print(my_list2[1:3])  # [100, 23.2]

# Cancut lists
my_list3 = my_list + my_list2
print(my_list3)  # [1, 2, 3, 'String', 100, 23.2]

# Change elements
my_list[0] = 5
print(my_list)  # [5, 2, 3]

# add new value
my_list.append(6)
print(my_list)  # [5, 2, 3, 6]

# Remove item from the list
pop_value = my_list.pop()
print(f"Pop value is {pop_value}")  # Pop value is 6
print(my_list)  # [5, 2, 3]

# Remove specific index
print(my_list.pop(0))  # 5
print(my_list)  # [2, 3]
my_list.pop(-1)
print(my_list)  # [2]

# Sort
alphabetic_list = ['a', 'e', 'x', 'b', 'c']
numeric_list = [4, 1, 8, 3]

# ascending
alphabetic_list.sort()
numeric_list.sort()

print(alphabetic_list)  # ['a', 'b', 'c', 'e', 'x']
print(numeric_list)  # [1, 3, 4, 8]

# descending
alphabetic_list.sort(reverse=True)
numeric_list.sort(reverse=True)

print(alphabetic_list)  # ['x', 'e', 'c', 'b', 'a']
print(numeric_list)  # [8, 4, 3, 1]

#  reverse method
alphabetic_list.reverse()
print(alphabetic_list)  # ['a', 'b', 'c', 'e', 'x']
