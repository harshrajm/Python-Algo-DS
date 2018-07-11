def coinChange(num,coins):
    if(num in coins):
        return 1;
    else:
        minCoins = num
    
        for x in coins:
            if(x<num):
                numOfCoins = 1 + coinChange(num-x,coins)
                if(numOfCoins < minCoins):
                    minCoins = numOfCoins
    return minCoins

print(coinChange(15,[10,5,1]))

        
 
 
 
 
 
 
coinChange(10,[1,5,10])        