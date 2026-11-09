N=int(input("Enter N numbers: "))
i=0
j=0
sum=0

while i<N:
    i=i+1
    n=int(input("Enter n: "))
    if n<0:
        break
    sum=sum+n
    if n>9 and n<100:
        j+=1

avg=sum/2

print("Sum: ",sum)
print("Dvucifreni chisla: ", j)
print("Sredno: ", avg)