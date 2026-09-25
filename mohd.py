def first_space(text):
    i = 0

    while i < len(text):
        if text[i] == ' ':
            return i
        i += 1

    raise ValueError
