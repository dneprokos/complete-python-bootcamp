def myfunc(a, b):
    return sum((a, b)) * 0.05


def myfunc_with_args(*args):  # args is not necessary. It can be any other param name, but it should start from '*'. E.g '*spam'
    return sum(args) * 0.05


result = myfunc_with_args(1, 2, 4, 5)
print(result)


def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("I haven't found any fruit")


myfunc(fruit='apple', veggie='lettuce')


def myfunc(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


myfunc(10, 20, 30, fruit='orange', food='eggs', animal='dog')
