string=input().strip()
dis_count=len(set(string))
if dis_count%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")