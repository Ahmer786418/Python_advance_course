p1 = "Make a lot of money"
p2 = "buy now"
p3 = "suscribe this"
p4 = "click this"

messege = input("Enter your comment : ") 


if((p1 in messege) or (p2 in  messege) or (p3 in messege) or (p4 in messege)):
    print("this comment is a spam")
    
else:
    print("this comment is not spam")