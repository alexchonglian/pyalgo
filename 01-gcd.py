def gcd(m,n):
  while m%n != 0:
    m,n = n,m%n
    print(m, n)
  return n

print(gcd(48, 34))