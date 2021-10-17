def reverse_number(number: int) -> int:
    s = 0
    while number != 0:
        last_digit = number % 10
        s = 10 * s + last_digit
        number = int(number / 10)

    return s


print(reverse_number(321))
