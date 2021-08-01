#Problem link:https://www.hackerrank.com/challenges/apple-and-orange/problem
#Problem name:Apple and Orange
#Status : Easy
#Solution
def countApplesAndOranges(s, t, a, b, apples, oranges):
    app=[a+x for x in apples]
    orr=[b+y for y in oranges]
    apple_count=0
    orange_count=0
    for i in app:
        if s<=i<=t:
            apple_count+=1
    for j in orr:
        if s<=j<=t:
            orange_count+=1
    print(apple_count)
    print(orange_count)

    
