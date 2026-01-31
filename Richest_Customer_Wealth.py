accounts = [[7,1,3], 
            [2,8,7],
            [1,9,5]]
sum=0

for element in range(len(accounts)):
    
    for subelement in accounts[element]:
        sum+=subelement
    print(sum)