from itertools import product
value=0
with open("day7.txt") as f:
    for line in f:
        line=line.strip().replace(":","").split()
        target=int(line[0])
        values=list(map(int, line[1:]))
        #@print(f'target {target}, values {values}')
        signs=("*","+")
        combinations=list(product(signs,repeat=len(values)-1))
        flag=False
        for combination in combinations:
            curr=values[0]
            for i in range(len(combination)):
                if combination[i]=="+":
                    curr+=values[i+1]
                else:
                    curr*=values[i+1]
            if curr==target:
                value+=target
                flag=True
                break
            if flag:
                break


print(value)