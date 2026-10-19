n = int(input("Enter number n: "))

odd_divisors = []

for i in range(1, n + 1):
  if n % i == 0 and i % 2 != 0:
    odd_divisors.append(i)

print(", ".join(map(str, odd_divisors)))