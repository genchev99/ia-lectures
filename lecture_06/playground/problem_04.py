def factorial(number: int) -> int:
    result = 1
    for x in range(1, number + 1):
        result *= x

    return result


print(factorial(5))
print(factorial(0))
print(factorial(1))
