n = int(input("Enter number n: "))

a, b = 1, 1
fib = []

while a <= n:
  fib.append(a)
  a, b = b, a + b

print(", ".join(map(str, fib)))