class Differential(Function):
  def get(self,x):
    f1 = super().get(x)
    f2 = super().get(x + 1e-8)
    return (f2-f1)/1e-8