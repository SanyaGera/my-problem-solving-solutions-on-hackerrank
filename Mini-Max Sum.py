#Problem link:https://www.hackerrank.com/challenges/mini-max-sum/problem
#Problem name: Mini-Max Sum
#Status:Easy
#Solution
def miniMaxSum(arr):
    arr.sort()
    Sum2=0
    for i in range(1,len(arr)):
        Sum2+=arr[i]
    arr.remove(arr[len(arr)-1])
    sum1=sum(arr)    
    ar=[]
    ar.append(sum1)
    ar.append(Sum2)
    print(*ar,sep=' ')
