result=set()
arr=[]
with open("day4.txt") as file:
    for line in file:
        line=line.strip()
        arr.append(line)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]=="M":
            for x,y in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                n_i,n_j=i+x,j+y
                if 0<=n_i<len(arr) and 0<=n_j<len(arr[0]) and arr[n_i][n_j]=="A":
                    p=0
                    valid=True
                    for a, b in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        a1,b1=n_i+a,n_j+b
                        a2,b2=n_i-a,n_j-b
                        if (0<=a1<len(arr) and 0<=b1<len(arr[0])) and (0<=a2<len(arr) and 0<=b2<len(arr[0])):
                            if arr[a1][b1]=="M" and arr[a2][b2]=="S" or arr[a1][b1]=="S" and arr[a2][b2]=="M":
                                p+=1
                            else:
                                valid=False

print(result)