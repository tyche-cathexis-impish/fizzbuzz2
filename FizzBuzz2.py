def fizzbuzz_convert(number):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"

    else:
        return str(number)


result = fizzbuzz_convert(1)

print(1)
