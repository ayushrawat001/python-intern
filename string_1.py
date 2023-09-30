st1="hello buddy welcome to python in JECRC"
print(st1)
print(type(st1)) #show the type of variable
print(len(st1)) #check length of st1
print("hello1" in st1)#for check giving word is available in the string or not 
print(st1.upper())#for uppercase
print(st1)
print(st1.lower())#for lowercase
t1=(1,2.43,"ayush",'a')#define a tuple and initialize
print(t1)
print(len(t1))
print(str(t1[1])+t1[2])#adding string to integar
l1=[1,34,2.45,2.33]#define a list and initialize
print(str(l1[1])+t1[3])
l1.append("jhkaas")#append is use for add an element in the end of list
print(l1)
l1.insert(3,21)#insert is use for add an element in the index of list which you want
print(l1)
#mutable data type:-int,float,string,tuple
#(mutable data is those data type which is change their values and data in place without effecting their identity)


#immutable data type:-list dictionary
#(immutable data is those data type which values and data can't change in place)