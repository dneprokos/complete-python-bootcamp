# MAP
def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)


print(list(map(square, my_nums)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))

# FILTER


def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, my_nums)))

# LAMBDA EXPRESSIONS


def square(num):
    result = num ** 2
    return result


print(lambda num: num ** 2)


print(list(map(lambda x: x[0], names)))
