new_string = 'Hello World!'
my_list = [letter for letter in new_string]
print(my_list);  # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']

range_list = [x for x in range(1, 11)]
print(range_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

range_list = [x**2 for x in range(1, 11)]
print(range_list)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

range_list = [x for x in range(1, 11) if x % 2 == 0]
print(range_list)  # [2, 4, 6, 8, 10]
