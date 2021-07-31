#Problem link:https://www.hackerrank.com/challenges/py-set-mutations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#Problem name:Set Mutations
#Status:Easy
n=int(input())
A=set(map(int,input().split()))
k=int(input())
for i in range(k):
    choice=input().split()
    B=set(map(int,input().split()))
    if choice[0]=="update":
        A.update(B)
    elif choice[0]=="intersection_update":
        A.intersection_update(B)
    elif choice[0]=="difference_update":
        A.difference_update(B)
    else:
        A.symmetric_difference_update(B)
print(sum(A))
