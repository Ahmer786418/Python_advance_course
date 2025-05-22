#  convert inchs to cm

def inch_To_cm(inch):
    return inch * 2.54

n = int(input("Enter the inches"))
print(f"the corresponding value of cms is {inch_To_cm(n)}")