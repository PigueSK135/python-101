def fizzbuzz(number):
    if number == 0:
        return number
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number

if __name__ == "__main__":
    print("ok")