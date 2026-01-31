num=int(input())
X=0
for i in range(num):
    x=input()
    if "++" in x:
        X+=1
    else:
        X-=1
print(X)