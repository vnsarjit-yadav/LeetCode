num=int(input())
for i in range(num):
    string=input()
    if len(string)<=10:
        print(string)

    else:
        print(string[0]+str(len(string)-2)+string[-1])