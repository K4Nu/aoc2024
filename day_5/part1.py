h_map={}
arr=[]
flag=True
c=0
with open("day5.txt") as file:
    for line in file:
        line=line.strip()
        if line=='':
            flag=False
        elif flag:
            a,b=map(int, line.split("|"))
            if b in h_map:
                h_map[b].append(a)
            else:
                h_map[b]=[a]
        else:
            curr=list(map(int,line.split(",")))
            arr.append(curr)
#print(h_map)
for i in range(len(arr)):
    flag=True
    for j in range(len(arr[i])):
        curr=arr[i][j]
        if curr not in h_map.keys():
            continue
        elif len(set(h_map[curr])&set(arr[i][j+1:]))>0:
            #print(curr,h_map[curr])
            flag=False
            break
    if flag:
        mid=(0+len(arr[i]))//2
        c+=arr[i][mid]
print(c)


