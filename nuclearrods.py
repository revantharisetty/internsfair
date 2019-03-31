import math
size=input()
size=int(size)
x=input()
x=int(x)
res=[]
for i in range(x):
    find=0
    lis=[]
    lis=input().split()
    if i ==0:
        res.append(lis)
        find=1
    else:
        for k in range(len(res)):
            for j in range(2):
                if lis[j] in res[k]:
                    res[k].append(lis[0])
                    res[k].append(lis[1])
                    find=1
                    break
    if find==0:
        res.append(lis)
total=0
done=0
for i in range(len(res)):
    res[i]=set(res[i])
    done=done+len(res[i])
    total=total+math.ceil(math.sqrt(len(res[i])))
#print(res)
total=total+size-done
print(total)
