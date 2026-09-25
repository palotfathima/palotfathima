def count_digits(n):
  if type(n) != int:
    raise ValueError

  if n == 0:
    return 1

  count = 0

  if n < 0:
    n = -n

  while n > 0:
    count += 1
    n = n // 10

  return count
