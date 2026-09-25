def count_evens(numbers):
    i = 0
    count = 0

    while i < len(numbers):
        if numbers[i] % 2 == 0:
            count += 1
        i += 1

    if count == 0:
        raise ValueError

    return count
