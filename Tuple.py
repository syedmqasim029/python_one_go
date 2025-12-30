# tup = tuple(["Qasim"])
# # or 
# tu = ('Qasim',"Abdullah")
# print(tup[0],len(tup))
# print(tu[:])

# If we want to change a. vallue of tuple it raises an error!
# tup[0] = "Abdullah"
# TypeError: 'tuple' object does not support item assignment

# We can change the value by re assigning the new tuple to same reference variable 
# tu = ("Abdullah","Ali","Rehman","Qasim")
# print(tu)
# i =0 
# while i < len(tu):
#     print(tu[i])
#     i+=1
# print()
# for i in tu:
#     print(i)
     
    
# # For adding new items we have to convert tuple into list the add variablles then convert to tuple again
# t = (1, 2, 3)

# lst = list(t)
# lst.append(4)

# t = tuple(lst)
# print(t)
