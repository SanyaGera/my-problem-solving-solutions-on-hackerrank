#Problem link:https://www.hackerrank.com/challenges/staircase/problem
#Problem name:Staircase
#Status: Easy
#Solution
def staircase(n):
    st='#'
    for i in range(1,n+1):
        x=st*i
        print(x.rjust(n))
