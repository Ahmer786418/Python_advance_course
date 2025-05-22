marks = {
  "ahmer" : 100,
  "rehan" : 98,
  "uzaid" : 56
}
print(marks.items()) 
    # they print like tuples in set form [('ahmer', 100 )] 
print(marks.values())
    #  they print only values of keys
marks.update({"ahmer" : 67, "khizer" : 98})
print(marks)
#  they updated old marks and add new person marks

# print(marks.get("ahmer2")) # print none,
# print(marks["ahmer2"])    # returns an error
#  pop or pop items

value = marks.pop("rehan")
print(value)
#  if i written here another which is not assigned here
#  it'll give error

