x = 0

# While-else loop
while x < 5:
    print(f"The current value of x is {x}")
    x += 1
else:
    print("X is not less than 5")

y = [1, 2, 3]

# pass keyword. Does nothing
for item in y:
    pass

name = 'Sammy'

# Continue. Jumps to the next loop iteration
for letter in name:
    if letter == 'a':
        continue
    print(letter)

# Break. Breaks a loop
for letter in name:
    if letter == 'a':
        break
    print(letter)







