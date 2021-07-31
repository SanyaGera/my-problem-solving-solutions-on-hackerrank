#Problem link:https://www.hackerrank.com/challenges/py-set-union/problem
#Problem name:Set .union() Operation
#Status : Easy
n=int(input())
english=set(map(int,input().split()))
k=int(input())
french=set(map(int,input().split()))
print(len(french.union(english)))
