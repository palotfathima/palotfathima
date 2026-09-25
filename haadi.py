def relations(n, numbers):
    result = []
    
    if n == 0:
        for num in numbers:
            result.append(num == 0)
        return result
    
    for num in numbers:
        result.append(num % n == 0)
    
    return result
