from value_operations import swap
from fizzbuzz import fizzbuzz

# print(__name__)
if __name__ == "__main__":
    # fruits = ["apple", "guava", "mango"]
    # [print("fruits[index] is", fruits[index], "also fruit is", fruit) for index, fruit in enumerate(fruits)]

    a = 5
    b = 10
    a, b = b, a
    # print(a, b)

    # print(swap("x", 2))

    [print(number + 1, fizzbuzz(number + 1)) for number in range(30)]
    [print(number, fizzbuzz(number)) for number in range(-30, 0)]