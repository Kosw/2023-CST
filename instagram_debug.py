def instagram_debug(a,b):
  s = set(zip(a,b))
  d = dict()
  for i, _ in s:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
  d1 = dict(sorted(d.items()))
  return d1