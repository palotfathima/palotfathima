def first_negative_value_index(numbers):
    i = 0

    while i < len(numbers):
        if numbers[i] < 0:
            return [numbers[i], i]
        i += 1

    raise ValueError
