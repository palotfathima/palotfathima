def sums(numbers):
    i = 0
    positive_sum = 0
    negative_sum = 0

    while i < len(numbers):
        if type(numbers[i]) != int:
            raise ValueError

        if numbers[i] > 0:
            positive_sum += numbers[i]
        elif numbers[i] < 0:
            negative_sum += numbers[i]

        i += 1

    return [positive_sum, negative_sum]
