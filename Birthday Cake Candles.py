#Problem link:https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r=next-challenge&h_v=zen
#Problem name:Birthday Cake Candles
#Status:Easy
#Solution
def birthdayCakeCandles(candles):
    candles.sort()
    count=1
    for i in range((len(candles)-2),-1,-1):
        if candles[i]==candles[len(candles)-1]:
            count+=1
        else:
            break
    return count
