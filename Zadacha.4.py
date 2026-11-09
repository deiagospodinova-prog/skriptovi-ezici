a=int(input("Enter a: "))
b=int(input("Enter b: "))

if a<=0 or b<=0:
    print("Nevalidni chisla")

while a>0 and b>0:
    nod=(b,a%b)
    if b==0:
        nod=a

nok=a*b/nod

if nod==1:
    print("Vzaimno prosti")
else:
    print("Ne sa vzaimno prosti")