c=0
with open("day2.txt") as file:
    for line in file:
        nums=list(map(int, line.strip().split()))
        flag=True
        d=nums[0]-nums[1]
        for i in range(len(nums)-1):
            val=nums[i]-nums[i+1]
            if abs(val)>3 or val==0 or val*d<0:
                print(nums[i],nums,d)
                flag=False
                break
        if flag:
            c+=1
print(c)