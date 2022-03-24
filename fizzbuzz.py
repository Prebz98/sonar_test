def fizzbuzz(number):
    res = ""
    if (number % 3 == 0):
        res += "Fizz"
    if (number % 5 == 0):
        res += "Buzz"
    if (res == ""):
        return number
    return res

def fizzbuzz_zero_to_hundred():
    for i in range(1, 100):
        print(fizzbuzz)
