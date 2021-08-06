#Problem link:https://www.hackerrank.com/challenges/sock-merchant/submissions/code/227052008?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#Problem name:Sales by Match
#Status:Easy
#Solution
def sockMerchant(n, ar):
    n=collections.Counter(ar)
    Sum=0
    for i in n.values():
        Sum+=i//2
    return Sum
