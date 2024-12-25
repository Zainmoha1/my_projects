# #practice 1
# def sum_of_list(list):
#     total=0
#     for i in list:
#         total+=i
#     return total
# print(sum_of_list([1,2,3,4,5]))

# def sum_of_list(list):
#     return sum(list)
# print(sum_of_list([1,2,3,4,5]))

# #practice 2
# def square_list_items(list):
#     list2=[]
#     for i in list:
#         list2.append(i**2)
#     return list2
# print(square_list_items([1,2,3,4,5]))

# def square_list_items(list):
#     return [i**2 for i in list]
# print(square_list_items([1,2,3,4,5]))

# #practice 3
# def remove_empty_string(list1):
#     t=[]
#     for i in list1:
#         if i.strip():
#             t+=i
#     return t
# print(remove_empty_string (['a','b','',' ','   ','c']))

# #practice 4
# def remove_duplicates(list1):
#     x=set(list1)
#     return list(x)
# print(remove_duplicates([1,2,3,3,3,4,5,6,"a","a"]))

# def remove_duplicates(list1):
#     List2=[]
#     for i in list1:
#         if i not in List2:
#             List2.append(i)
#     return List2
# print(remove_duplicates([1,2,3,3,3,4,5,6,"a","a"]))

#practice 5
def have_common_members(list1,list2):
    x=list1+list2
    z=set(x)
    y=list(z)
    y.sort()
    if x==y:
        return False
    else:
        return True
print(have_common_members(['a','b','c','d'],['e','f','g']))

def have_common_members(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                return True
            else:
                return False
print(have_common_members(['a','b','c','d'],['e','f','g']))

