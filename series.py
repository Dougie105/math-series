# Fibonacci Function

def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

# Lucas Function

def lucas(r):
  if r == 0:
    return 2
  if r == 1:
    return 1
  return lucas(r-1) + lucas(r-2)

# Sum Series Function

def sum_series(x, y=0, z=1):
  if x == 2:
    return y
  if x == 1:
    return z
  return sum_series(x-1, y, z) + sum_series(x-2, y, z)