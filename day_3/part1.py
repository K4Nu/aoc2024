import re
value=0
with open("day3.txt") as file:
    for line in file:
        line=line.strip()
        pattern=r"mul\(\d+,\d+\)"
        p=re.findall(pattern,line)
        for match in p:
            x=match[match.index("(")+1:match.index(")")]
            x,y=map(int,x.split(","))
            value+=x*y
print(value)