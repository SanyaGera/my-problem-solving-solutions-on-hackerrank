#Problem link:https://www.hackerrank.com/challenges/plus-minus/problem
#Problem name:Plus Minus
#Status:Easy
#Soluion
positive=0
negative=0
zeros=0
n=len(arr)
for i in arr:
  if i<0:
    negative+=1
  elif i>0:
    positive+=1
  else:
    zeros+=1
print(positive/n)
print(negative/n)
print(zeros/n)
