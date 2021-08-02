#Problem link:https://www.hackerrank.com/challenges/utopian-tree/problem?h_r=next-challenge&h_v=zen
#Problem name:Utopian Tree
#Status: Easy
#Solution
def utopianTree(n):
    h=1
    for i in range(n):
        if i%2==0:
            h=h*2
        else:
            h=h+1
    return h
