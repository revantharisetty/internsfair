x=input()
x=int(x)
res=[]
lis=[]

for i in range(x):
    instruction=input()
    instruction=instruction.split()
    if(len(instruction)==1):
        
        if len(lis)==1:
            #print("EMPTY")
            res.append("EMPTY")
            lis.pop(len(lis)-1)
        elif len(lis)==0:
            res.append("EMPTY")
        else:
            lis.pop(len(lis)-1)
            #print(lis[len(lis)-1])
            res.append(lis[len(lis)-1])
    elif (len(instruction)==2):
        lis.append(instruction[1])
        res.append(lis[len(lis)-1])
        #print(lis[len(lis)-1])
    else:
        temp=0
        for m in range(int(instruction[1])):
            lis[temp]=int(lis[temp])+int(instruction[2])
            temp=temp+1
        #print(lis[len(lis)-1])
        res.append(lis[len(lis)-1])
for i in range(len(lis)):
    print(str(lis[i]))
