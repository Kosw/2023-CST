class Differential(Function):
  def get(self, a):
    b = 1e-8
    f1 = super().get(a+b)
    f2 = super().get(a-b)
    return ((f1-f2)/(2*b))