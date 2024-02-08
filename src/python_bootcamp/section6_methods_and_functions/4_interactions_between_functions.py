from random import shuffle

example = [1, 2, 3, 4, 5, 6, 7]
shuffle(example)
print(example)  # Will return shuffled list


def shuffle_list(some_list):
    shuffle(some_list)
    return some_list


print(shuffle_list(example))

my_list = [' ', 'O', ' ']


def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1 or 2")

    return int(guess)


player_guess()
