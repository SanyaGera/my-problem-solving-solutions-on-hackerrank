#Problem link:https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
#Problem name:Divisible Sum Pairs
#Status:Easy
#Solution
def divisibleSumPairs(n, k, ar):
    Count=0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k==0:
                Count+=1
    return Count
