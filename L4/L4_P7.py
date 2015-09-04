# p1
def foo(x):
  def bar(x):
    return x+1
  return bar(x*2)
print( foo(3) )

# p2
def foo(x):
  def bar(z):
    return z + x
  return bar(3)
print( foo(2) )
