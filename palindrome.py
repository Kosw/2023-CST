class palindrome:
  count = 0
  def check(self, s):
    if s == s[::-1]:
      palindrome.count += 1
  def __str__(self):
    return str(palindrome.count)