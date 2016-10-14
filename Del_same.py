# List=['a','a','b','c','b','c']
# print("Before:",List)
# if List:
#     List.sort()
#     last = List[-1]
#     for i in range(len(List)-2,-1,-1):
#         if  last == List[i]:
#             del List[i]
#         else:
#             last=List[i]
# print("After:",List)

l1=['a','a','b','c','b','c']
print("Before:",l1)
l2=[]
[l2.append(i) for i in l1 if not i in l2]
print("After:",l2)