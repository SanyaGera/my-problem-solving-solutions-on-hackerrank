#Probelm link:https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
#Problem name:Set .discard(), .remove() & .pop()
#Status:Easy
n = int(input())
s = set(map(int, input().split()))
k=int(input())
for i in range(k):
    choice=input().split()
    if choice[0]=="pop":
        s.pop()
    elif choice[0]=="remove":
        s.remove(int(choice[1]))
    else:
        s.discard(int(choice[1]))
print(sum(s)) 
    

