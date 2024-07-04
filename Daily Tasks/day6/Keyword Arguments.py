#Keyword Arguments

def show(**num):
    for i, j in num.items():
        print(i, j)
show(n1=10, n2=20)