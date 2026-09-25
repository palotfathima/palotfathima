def reverse_digits(n):
    if type(n) != int:
        raise ValueError

    sign = 1

    if n < 0:
        sign = -1
        n = -n

    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return sign * reverse
