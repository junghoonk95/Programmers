def solution(d, budget):
    arr=sorted(d)
    sol=0
    cnt=0
    for i in arr:
        sol=sol+i
        if sol>budget:
            break
        cnt=cnt+1
    return cnt
