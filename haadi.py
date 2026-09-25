def first_letters(strings):
    result = ""
    
    for s in strings:
        if s == "":
            raise ValueError
        result += s[0]
    
    return result
