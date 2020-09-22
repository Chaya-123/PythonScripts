l1=[]
l2=[]
x1=input("enter the first element to insert into list l1:")
l1.append(x1)
x2=input("enter the first element to insert into list l2:")
l2.append(x2)
x3=input("enter the second element to insert into list l1:")
l1.append(x3)
x4=input("enter the second element to insert into list l2:")
l2.append(x4)
print("Assigning elements to different list")
print("list l1:",l1)
print("list l2:",l2)
tup=('C','C++','Java')
print(tup)
print("elements of the tuple are:")
for i,x in enumerate(tup):
    print(i+1,"th element is:",x)
x=int(input("Enter the index to retrive its value in the tuple"))
print(tup[x-1])
            
dict={"Name":"Chaya","Occupation":"Student","Age":20,"Address":"Bangalore"}
print("Dictionary is:",dict)
x=input("enter the index to be deleted")
del dict[x]
print("After deleting "+x+"the dictionary is",dict)
    

