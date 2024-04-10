def fizz_buzz():
    n = int(input("Number: "))
    for x in range(1, n):
        if x % 3 == 0 and x % 5 == 0:
            x = print("FizzBuzz")
        elif x % 3 == 0:
            x = print("Fizz")
        elif x % 5 == 0:
            x = print("Buzz")
        else:
            print(x)


fizz_buzz()
