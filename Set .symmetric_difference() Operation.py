#Probelm link:https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#Problem name:Set .symmetric_difference() Operation
#Status:Easy
n=int(input())
english=set(map(int,input().split()))
k=int(input())
french=set(map(int,input().split()))
print(len(english.symmetric_difference(french)))

