def fact(n):
  if n > 1:
     factorial = n*fact(n-1)
  elif n == 1 or n == 0:
      return 1
  return factorial
x = fact(4)
print(x)
