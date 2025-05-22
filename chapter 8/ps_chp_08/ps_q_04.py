# cal sum of 1ST n natural number

"""
# sum(n) = 1+2+3+4 


"""


def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(4))





