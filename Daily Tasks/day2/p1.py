a = int(input('Enter the no: '))
b = int(input('Enter the no: '))
c = int(input('Enter the no: '))
d = int(input('Enter the no: '))
     
if a>b and a>c and a>d:
    print(a, "is greatest no")
elif b>c and b>d:
    print(b, "is greatest no")
elif c>d:
    print(c, "is greatest no")
else :
    print(d, "is greatest no")