def even_check(number):
    return number % 2 == 0


print(even_check(20))  # TRUE
print(even_check(21))  # FALSE


def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
    else:
        pass


print(check_even_list([1, 3, 5]))  # Returns nothing
print(check_even_list([2, 3, 4]))  # Returns True


def check_even_list2(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True

    return False


print(check_even_list2([1, 3, 5]))  # Returns False
print(check_even_list2([2, 3, 4]))  # Returns True
