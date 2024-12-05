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
            if a in h_map:
                h_map[a].append(b)
            else:
                h_map[a]=[b]
        else:
            curr=list(map(int,line.split(",")))
            arr.append(curr)
print(h_map)
for i in range(len(arr)):
    flag=True
    for j in range(len(arr[i])):
        curr=arr[i][j]
        if curr not in h_map:
            continue
        elif len(set(h_map[curr])&set(arr[i][:j]))>0:
            flag=False
            break
    if flag==False:
        new_arr=[]
        for ind in range(len(arr[i])):
            temp=ind
            while temp>0:
                if arr[i][ind] not in h_map or len(set(h_map[arr[i][ind]])&set(new_arr[:temp]))==0:
                    break
                else:
                    temp-=1
            new_arr.insert(temp,arr[i][ind])
        mid=(0+len(arr[i]))//2
        c+=new_arr[mid]

print(c)