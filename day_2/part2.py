c=0
def is_safe(nums):
    d = nums[0] - nums[1]
    for i in range(len(nums) - 1):
        val = nums[i] - nums[i + 1]
        if abs(val) > 3 or val == 0 or val * d < 0:
            return False
    return True
with open("day2.txt") as file:
    for line in file:
        nums=list(map(int, line.strip().split()))
        if is_safe(nums):
            c+=1
            continue
        found_safe=False
        for i in range(len(nums)):
            new_nums=nums[:i]+nums[i+1:]
            if is_safe(new_nums):
                found_safe=True
                break
        if found_safe:
            c+=1
print(c)

