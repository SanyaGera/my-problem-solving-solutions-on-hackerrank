#Problem link:https://www.hackerrank.com/challenges/py-set-add/problem
#Problem name:Set .add()
#Status:Easy
N=int(input())
s=set()
for i in range(N):
    x=str(input())
    s.add(x)
print(len(s))
