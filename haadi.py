def relations(n, numbers):
    result = []
    
    for num in numbers:
        if num == 0:
            result.append(True)
        else:
            result.append(num % n == 0)
    
    return result
