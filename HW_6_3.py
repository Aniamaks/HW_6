number = int(input("Введіть ціле число: "))

while number > 9:
    result = 1

    while number > 0:
        digit = number % 10
        result *= digit
        number //= 10

    number = result

print(number)