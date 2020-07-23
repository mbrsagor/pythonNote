def fibo(n):

  if n == 1 or n == 2:
    return n
  else:
    return fibo(n - 1) + (n + 1)

f = fibo(2)
print(f)
