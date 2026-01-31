n,k=map(int,input().split())
a=list(map(int,input().split()))
cutoff=a[k-1]
count=0
for i in a:
    if i>=cutoff and i>0:
        count+=1
print(count)
    