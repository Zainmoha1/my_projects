# try:
#     numbers=[1,2,3,4,5,6,7,8]
#     print(numbers[10])
# except IndexError:
#     print('index ka baxsan kalisey')

# numbers=[1,2,3,4,5]
# numbers[-1]="Maxaa ii dhiibatay".title()
# print(numbers)

# numbers=[1,2,3,4,5]
# x=numbers[-1]+numbers[-2]
# print(x)

# numbers=['a','b','c','d','e','f','g','h']
# print(numbers[2:5])
# print(numbers[:4])
# print(numbers[3:6])
# print(numbers[5:])
# print(numbers[-4:])

# numbers=['a','b','c','d','e','f','g','h']
# if 'b' in numbers:
#     print("yes")
# else:
#     print("no")

# numbers=[1,2,3]
# for i in range(4,11):
#     numbers.append(i)
# print(numbers)

# numbers=[10,20,30,40,50,70,80,90]
# index=numbers.index(70)
# numbers.insert(index,60)
# print(numbers)

# numbers=[10,20,30,40,50,70,80,90]
# w = numbers.pop()
# print(w)

# letters=['t','a','k','wh','name']
# M=[]
# for i in letters:
#     M.append(i)
# print(M)

def square_sum(list):
    total=[]
    for i in list:
        total.append(i**2)
    return total       
print(square_sum([1,2,3]))

# def square_sum(list):
#     return sum([i**2 for i in list])
# print(square_sum([1,2,3]))










def square_sum(list):
    list2=[i**2 for i in list]
    total=0
    for k in list2:
        total+=k
    return total    
print(square_sum([1,2,3]))