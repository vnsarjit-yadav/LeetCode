problem=int(input())
count=0
for que in range(problem):
    # enter only 0 and 1 for solve problem
    a,b,c=map(int, input().split())
    
    if a+b+c>=2:
        count+=1
print(count)
