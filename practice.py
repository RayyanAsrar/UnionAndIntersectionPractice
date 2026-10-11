#############intersection practice########
# a=[1,2,3,4,5]
# b=[9,5,2]
# intersection_list=[0,0,0]
# inter_index=0
#####WAY 1########
# for x in range(len(b)):
#     for y in range(len(a)):
#         if b[x]==a[y] :
#             intersection_list[inter_index]=b[x]
#             inter_index=inter_index + 1
# print(intersection_list)
#######WAY 2########
# for newb in b:
#     for newa in a:
#         if newb==newa :
#              intersection_list[inter_index]=newb
#              inter_index=inter_index + 1
# print(intersection_list)
#####union#########

################## SIR WALA CODE ############
# a=[1,2,3,4]
# b=[2,4,7]
# union=[0,0,0,0,0]
# for i in range (4):
#   union[i]=a[i]
# z=i;
# for y in range (3):
#   flag=0
#   for y1 in range (len(union)):
#     if (b[y]==union[y1]):
#       flag=1
#   if (flag==0):
#     z=z+1
#     union[z]=b[y]
#     z=z+1
# print(union)


#############RAYYAN BHAI KI WRONG APPROACH 1 ##############
#union practice 
# a=[1,3,4,9]
# b=[2,3,7,5]
# union=[0,0,0,0,0,0,0] #index= 3
# union_ind=0

# for newa in a:
#     union[union_ind]=newa
#     union_ind=union_ind+1
    
# for newb in b:
    
#     for newunion in union:  #[1, 3, 4, 9, 0, 0, 0]
        
#         if(newb==newunion):
#             continue
#         else:
#                 union[union_ind]=newb
#                 # print("checkpost1",union)
#                 union_ind=union_ind + 1
#                 print("checkpost2",union)
#                 # print("sabbse last wala ind",union_ind)


# print(union)
########### RAYYAN KI WRONG APPROACH 2 ############
# a=[1,3,4,9]
# b=[2,3,7,5]
# union=[0,0,0,0,0,0,0] #index= 3
# union_ind=0

# for newa in a:
#     union[union_ind]=newa
#     union_ind=union_ind+1
#     # print("pehla loop mai ind",union_ind)
# for newb in b:
#     # print("dusre loop mai ind",union_ind)
#     for newunion in union:  #[1, 3, 4, 9, 0, 0, 0]
#         # print("if se upar wale third loop mai ind",union_ind)
#         if(newb==newunion):
#             print("ye to match kar gya")
#             continue
#         else:
#                 union[union_ind]=newb
                
                
#                 # print("sabbse last wala ind",union_ind)
# union_ind=union_ind+1
# print(union)

a=[1,3,4,9]
b=[2,3,7,5]
union=[0,0,0,0,0,0,0] #yahan pe index= 3 tak bhara hua hai 
union_ind=0

for newa in a:
    union[union_ind] = newa
    union_ind = union_ind + 1 # yahan last union_ind = 4 hai 

for newb in b:  # yahan pe union kuch aesa dikh raha [1, 3, 4, 9, 0, 0, 0]
    found=False
    for i in range(union_ind): #yahan par union_ind=4 
        if union[i]==newb:
            found=True
            break
    if(found!=True):
        union[union_ind]=newb
        union_ind=union_ind+1
print("ye agya UNION",union) 
