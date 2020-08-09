
s=(input(print("input the file name:")))
d=s.split(".")

for x in d:
    if x=="py":
        print("The extension of the file is:python")
    elif x=="c":
        print("The extension of the file is:c")
    elif x=="c++" or x=="cpp":
        print("The extension of the file is:c++")
    elif x=="java":
        print("The extension of the file is:java")
    elif x=="jpeg":
        print("The extension of the file is:image")
    elif x=="txt":
        print("The extension of the file is:text")
    else:
        print()
    
