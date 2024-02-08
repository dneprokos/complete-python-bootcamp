def say_hello():
    print("Hello")
    print("World")


say_hello()


def say_hello(name="<No_Name>"):
    print(f"Hello {name}")


say_hello("Kostia")  # Hello Kostia
say_hello()  # Hello <No_Name>


def add_num(num1, num2):
    return num1 + num2


result = add_num(3, 7)
result2 = add_num('5', '5')
print(result)  # 10
print(result2)  # 55


