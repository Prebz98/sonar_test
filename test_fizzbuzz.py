from fizzbuzz import fizzbuzz

def test_fizz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(18) == "Fizz"
    assert fizzbuzz(48) == "Fizz"
    assert fizzbuzz(33) == "Fizz"
    

def test_buzz():
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(25) == "Buzz"
    assert fizzbuzz(55) == "Buzz"
    assert fizzbuzz(80) == "Buzz"
    
def test_common():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"
    assert fizzbuzz(90) == "FizzBuzz"
    
def test_miss():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(7) == 7
    assert fizzbuzz(91) == 91
    
    
def green_traffic_light_pattern():
    return 'All tests passed'


if __name__ == '__main__':
    test_fizz()
    test_buzz()
    test_common()
    test_miss()
    print(green_traffic_light_pattern())
