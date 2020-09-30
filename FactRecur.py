def fact(n):
  if n > 1:
     #Factorial of n = n * (n-1) * (n-2) *....*(2) * (1)
     factorial = n*fact(n-1)
  #Factorial of 1 and 0 is 1
  elif n == 1 or n == 0:
      return 1
  return factorial

#x = fact(4)
#print(x)

#Take input
x = input(" Type a number : ")
#Print factorial
print(fact(int(x)))

