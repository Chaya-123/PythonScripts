def most_frequent(s):
    d={}

    for i in str:
        
        if i in d:
            
            d[i]+=1
        else:
            
            d[i]=1
    d1=sorted(d,key=d.get,reverse=True)
    for i in d1:
        print(i,"=",d[i])
    

str=input("enter the string:")
most_frequent(str)



        
