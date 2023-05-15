def div(a, b):
  try:
    if b == 0:
      c = 0
    else:
      c = a / b
  except:
    c = "False"
  return c