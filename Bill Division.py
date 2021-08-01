#Problem link:https://www.hackerrank.com/challenges/bon-appetit/problem
#Problem name:Bill Division
#Status:Easy
#Solution
def bonAppetit(bill, k, b):
    
    S=(sum(bill)-bill[k])//2
    if b==S:
        print('Bon Appetit')
    else:
        print(b-S)
