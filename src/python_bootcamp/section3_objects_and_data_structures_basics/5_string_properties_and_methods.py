name = "Sam"

# Strings in Python are immutable
# name[0] = 'P' will throw an error

last_letters = name[1:]
name = 'P' + last_letters  # Cancat string
print(name)  # Pam

print('2' + '3')  # 23

x = 'Hello World'
print(x.upper())  # HELLO WORLD
print(x.lower())  # hello world
print(x.split())  # ['Hello', 'World']
print(x.split('W'))  # ['Hello ', 'orld']

