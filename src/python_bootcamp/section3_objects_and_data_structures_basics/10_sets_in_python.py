my_set = set()

my_set.add(1)
print(my_set)  # {1}
my_set.add(2)
print(my_set)  # {1, 2}
my_set.add(2)  # Will not be added, because set should contain unique values
print(my_set)  # {1, 2}

# Casting list to set
my_list = [1, 2, 1, 1, 2, 3, 4, 1, 11]
new_set = set(my_list)
print(new_set)  # {1, 2, 3, 4, 11}

