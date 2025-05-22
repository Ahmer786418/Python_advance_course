# write a prg using func to find greatest of three no.


def greatest(a,b,c):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a =100
b= 200
c= 300

print(greatest(a,b,c))