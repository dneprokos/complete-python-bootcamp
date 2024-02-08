x = 25


def printer():
    x = 50 # inner scope.
    y = 40
    return x


print(x)  # prints 25


name = 'This is a global string'


def greet():
    name = 'Sammy'

    def hello():
        print(f"Hello {name}")

    hello()


greet()  # Hello Sammy
