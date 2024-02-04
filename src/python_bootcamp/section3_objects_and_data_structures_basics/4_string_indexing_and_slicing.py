hello_world = 'Hello World!'

print(hello_world[0])  # H
print(hello_world[-1])  # !
print(hello_world[-2])  # d

alphabet_string = 'abcdefghijk'

print(alphabet_string[2:])  # cdefghijk
print(alphabet_string[:3])  # abc
print(alphabet_string[3:6])  # def
print(alphabet_string[1:3])  # bc

print(alphabet_string[::2])  # Step-size. Result: acegik

# string[start:stop: step_size]

# revert a string
print(alphabet_string[::-1])  # kjihgfedcba
