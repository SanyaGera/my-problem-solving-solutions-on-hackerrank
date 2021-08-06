#Problem link:https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#Problem name:Repeated String
#Status:Easy
#Solution
repeatedString(s, n):
    Count=0
    for i in s:
        if i=="a":
            Count+=1
    Count=Count*(n//len(s))
    for x in s[:n%len(s)]:
        if x=='a':
            Count+=1
    return Count
