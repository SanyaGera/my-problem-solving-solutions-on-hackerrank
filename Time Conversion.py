#Problem link:https://www.hackerrank.com/challenges/time-conversion/problem
#Problem name:Time Conversion
#Status:Easy
#Solution
def timeConversion(s):
    l=s[8:]
    if l=="AM" and s[:2]!="12":
        st=s[:8]
    elif l=='AM' and s[:2]=='12':
        st='00'+s[2:8]
    elif l=='PM' and s[:2]!='12':
        x=int(s[:2])
        x+=12
        st=str(x)+s[2:8]
    else:
        st=s[:8]
    return st
