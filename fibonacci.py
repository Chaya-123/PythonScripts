n=int(input("enter the no of terms:"))
f1=0
f2=1
i=2
print(f1,f2,end=',')
while(i<n):
    f3=f1+f2
    print(f3,end=',')
    f1=f2
    f2=f3
    i=i+1

     
