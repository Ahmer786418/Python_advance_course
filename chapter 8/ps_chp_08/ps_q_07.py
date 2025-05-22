def  rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n 

l = ["harry", "Rohan","shubam","an"]

print(rem(l,"an"))