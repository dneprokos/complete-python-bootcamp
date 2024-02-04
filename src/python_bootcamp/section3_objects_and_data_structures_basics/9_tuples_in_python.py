my_tuple = (1, 2, 3)
my_tuple2 = (1, "string", 45.5)
my_list = [1, 2, 3]

# Print
print(my_tuple)  # (1, 2, 3)
print(my_tuple2)  # (1, 'string', 45.5)
print(my_list)  # [1, 2, 3]

# print type
print(type(my_tuple))  # <class 'tuple'>
print(type(my_list))  # <class 'list'>

# Tuple methods
t = ('a', 'a', 'b')
print(t.count('a'))  # Show 2 because tuple contains two a
print(t.index('a'))  # 0. Return first index appearance

# t[0] = 'NEW' TypeError
