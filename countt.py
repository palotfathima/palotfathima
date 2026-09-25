def count_all(numbers):
    i = 0
    negative = 0
    zero = 0
    positive = 0

    while i < len(numbers):
        if numbers[i] < 0:
            negative += 1
        elif numbers[i] == 0:
            zero += 1
        else:
            positive += 1

        i += 1

    if len(numbers) == 0:
        raise ValueError

    return [negative, zero, positive]
