# simple way
# f = int(input("enter the temperature  :"))
# c = 5*(f-32)/9
# print(c)


# using function cel to far convertion 
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("enter the temperature in F :"))
c = f_to_c(f)
print(f"{round(c ,2) }  °C") 



