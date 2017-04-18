def fizz_buzz(number):
    assert(isinstance(number, int))
    if not number % 3 and not number % 5:
        return "FizzBuzz"
    if not number % 3:
        return "Fizz"
    if not number % 5:
        return "Buzz"
    return number