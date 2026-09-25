def first_even_index(numbers):
    i = 0
    
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            return i
        i += 1
    
