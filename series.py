# Fibonacci Function

def fibonacci(n):
  '''The function should have one parameter n. The function should return the nth value in the fibonacci series using recursion or iteration.'''
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Lucas Function

def lucas(r):
  '''Returns the nth value in the lucas numbers Again, you may use recursion or iteration'''
  if r == 0:
    return 2
  if r == 1:
    return 1
  return lucas(r-1) + lucas(r-2)

# Sum Series Function

def sum_series(x, y=0, z=1):
  '''Function with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.'''
  if x == 0:
    return y
  if x == 1:
    return z
  return sum_series(x-1, y, z) + sum_series(x-2, y, z)