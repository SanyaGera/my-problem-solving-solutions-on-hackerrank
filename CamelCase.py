#Problem link:https://www.hackerrank.com/challenges/camelcase/problem
#Problem name:CamelCase
#Status:Easy
#Solution
def camelcase(s):
    Count=1
    for i in s:
        if i.isupper():
            Count+=1
    return Count
