#Problem link:https://www.hackerrank.com/challenges/two-strings/problem?h_r=internal-search
#Problem name:Two Strings
#Status:Easy
#Solution
def twostrings(s1,s2):
    if(set(s1) & set(s2)):
        return 'YES'
    else:
        return 'NO'
