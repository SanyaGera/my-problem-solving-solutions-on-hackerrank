#Problem link:https://www.hackerrank.com/challenges/the-hurdle-race/problem
#Problem name:The Hurdle Race
#Status:Easy
#Solution
def hurdleRace(k, height):
    height.sort()
    n=len(height)
    b=height[n-1]
    if k>=b:
        return('0')
    else:
        return(b-k)
