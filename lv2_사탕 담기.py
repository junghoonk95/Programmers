from itertools import *
def solution(n):
    arr=[True for i in range(n+1)]
    arr[0] , arr[1] =False,False
    
    for i in range(2,int(n//2)+1):
        if arr[i]:
            j=2
            while i*j<=n:
                arr[i*j]=False
                j=j+1
    
    a=[p for p,q in enumerate(arr) if q==True]
    
    return (len([sum(c) for c in combinations(a,3) if sum(c)==n]))
            
