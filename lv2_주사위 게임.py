from itertools import*
def solution(monster, S1, S2, S3):
    a=len([sum(c) for c in list(product([i+1 for i in range(S1)],[j+1 for j in range(S2)],[i+1 for i in range(S3)])) if sum(c)+1 in monster])
    total=S1*S2*S3
    return int(1000*(total-a)/total)
