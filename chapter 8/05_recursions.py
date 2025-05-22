#  using factorial on function
#  almost using recursion for algorithms    
def factorial(n:int):
     if(n==1 or n==0):
       return 1
     return n*factorial(n-1)

n =int(input("enter a number :"))
print(f"the factorial of this no is : {factorial(n)}")     
 