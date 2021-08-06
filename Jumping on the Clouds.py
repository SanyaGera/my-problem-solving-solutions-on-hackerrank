#Problem link:https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#Problem name:Jumping on the Clouds
#Status:Easy
#Solution
def jumpingOnClouds(c):
    jumps=0
    current_position=0
    last_position=len(c)-1
    second_last_position=len(c)-2
    while current_position<second_last_position:
        if c[current_position+2]==0:
            jumps+=1
            current_position+=2
        else:
            jumps+=1
            current_position+=1
    if current_position==second_last_position:
        jumps+=1
    return jumps
