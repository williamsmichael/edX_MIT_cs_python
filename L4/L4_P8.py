def square(x):
  ''' x: into or float. '''
  return x ** 2

def fourthPower(x):
  ''' x: int or float. '''
  return square(square(x))

print( fourthPower(2) )
