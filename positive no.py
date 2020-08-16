l=[]
n=int(input("enter the no of elements in the list:"))
print("enter the elements:")
for i in range(0,n):
        ele=int(input())
        l.append(ele)
print(l)
for i in l:
        if(i>0):
         print(i,end=',')
