# H=input("ENTER Y OR N: ")
# while H=="Y":
#     print("THANKS")
#     H=input("ENTER Y OR N: ")
# START=int(input("INPUT STARTING POINT: "))
# while START<10:
#     print(START)
#     START-=1 
# prtm = True
# while prtm : 
#     entry = input('xisaabo soo gali oo leh operator : '  )
#     print(' jawaabtu waa :',eval(entry))
#     prtm = input('Ma rabtaa in wax kale xisaab [haa/mya]  : ')
#     if prtm == 'haa':
#         prtm = True
#     else:
#         prtm = False
# name = 'khaalid'
# binary = [bin(ord(name[i]))[2:] for i in range(len(name))]
# print(' '.join(binary))
# START=int(input(" INPUT STARTING POINT: "))
# END=int(input(" INPUT ENDING POINT: "))
# STEP=int(input(" INPUT STEP POINT: "))
# for i in range(START,END,STEP):
#     print(i)
START=int(input("INPUT STARTING POINT: "))
END=int(input("INPUT ENDING POINT: "))
# STEP=int(input(" INPUT STEP POINT: "))
sum = 0
for i in range(START,END):
    sum+=i
print(sum)
# 1 ,2 , 3 , 4, 5 sum between 1 and 5 
# 1 ,2 , 3 , 4 , 5 sum of the  1 up to 5 12