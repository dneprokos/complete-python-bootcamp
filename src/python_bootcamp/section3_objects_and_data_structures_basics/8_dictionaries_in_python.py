# Dictionaries uses key value pairs { 'key1': value1, 'key2':value2 }
my_dict = {'key1': 'value1', 'key2': 'value2'}

# get value
print(my_dict['key1'])  # value1

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup.keys())  # dict_keys(['apple', 'oranges', 'milk'])
print(prices_lookup.values())  # dict_values([2.99, 1.99, 5.8])
print(prices_lookup.items())  # {'apple': 2.99, 'oranges': 1.99, 'milk': 5.8, 'bread': 0.99}

# adding new values
prices_lookup['bread'] = 0.99
print(prices_lookup)  # {'apple': 2.99, 'oranges': 1.99, 'milk': 5.8, 'bread': 0.99}
