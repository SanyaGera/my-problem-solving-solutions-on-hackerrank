#Problem link:https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?h_r=next-challenge&h_v=zen
#Problem nameSet .intersection() Operation
#Status:Easy
n=int(input())
english=set(map(int,input().split()))
k=int(input())
french=set(map(int,input().split()))
print(len(english.intersection(french)))

