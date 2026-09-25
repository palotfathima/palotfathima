def min_max(l1):
  i = 0
  count = 0

  while i < len(l1):
    if type(l1[i]) != int:
      raise ValueError
    else:
      i += 1

  i = 0
  l2 = []
  l3 = []

  while i < len(l1):
    if l1[i] >= 0:
      l2.append(l1[i])
    elif l1[i] < 0:
      l3.append(l1[i])
    i += 1

  if len(l2) == 0:
    raise ValueError

  if len(l3) == 0:
    raise ValueError

  return [min(l2), max(l3)]
