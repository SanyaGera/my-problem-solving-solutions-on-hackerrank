#Problem link:https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#Problem name:Counting Valleys
#Status: Easy
#Solution
def countingValleys(steps, path):
    Count=0
    Valley=0
    for i in path:
        if i=='U':
            Count+=1
            if Count==0:
                Valley+=1
        elif i=='D':
            Count-=1
            
    return Valley
