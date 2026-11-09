N=int(input("Enter N numbers: "))
i=0
max_odd=0
sum=0

while i<N:
    i+=1
    n=int(input("Enter n: "))
    if N<=0:
        print("Nevaliden broi")
        break

    if n%2==0:
        sum=sum+n
    elif n>max_odd:
        max_odd=n
    else:
        print("Nqma nechetni chisla")

print("Sum: ", sum)
print("Nai golqmo nechetno (ako ima): ", max_odd)


