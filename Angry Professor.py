#Problem iink:https://www.hackerrank.com/challenges/angry-professor/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#Problem name:Angry Professor
#Status:Easy
#Solution
def angryProfessor(k, a):
    a.sort()
    Count=0
    for i in a:
        if i<=0:
            Count+=1
    if Count>=k:
        return ('NO')
    else:
        return('YES')
