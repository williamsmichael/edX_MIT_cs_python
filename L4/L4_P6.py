# p1
a = 10
def f(x):
  return x + a
a = 3
print(f(1))

# p2
x = 12
def g(x):
  x = x + 1
  def h(y):
    return x + y
  return h(6)
print( g(x) )
