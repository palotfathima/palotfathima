def count_floats_others(items):
    i = 0
    floats = 0
    others = 0

    while i < len(items):
        if type(items[i]) == float:
            floats += 1
        else:
            others += 1

        i += 1

    if len(items) == 0:
        raise ValueError

    return [floats, others]
