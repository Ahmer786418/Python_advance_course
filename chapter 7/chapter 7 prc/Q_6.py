# 5! = 1X 2X 3X 4X 5X 

n = int(input("Enter your number: "))
product = 1
for i in range(   1 ,  n+1):
    product = product*i

print(f"the factorial of {n} is {product}")