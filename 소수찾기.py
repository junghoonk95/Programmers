from itertools import*
import math
def getprime(x):
    if x<=1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
    
def solution(numbers):
    anw=[]
    cnt=0
    num=[]
    answer=[]
    for i in numbers:
        num.append(i)
        
    for i in range(1,len(numbers)+1):
        answer.extend(list(permutations(num,i)))
    answer=list(set(answer))
    
    for i in answer:
        obj=""
        for j in i:
            obj=obj+j
        print(int(obj))
        if getprime(int(obj))==True:
            anw.append(int(obj))
            
    print(sorted(list(set(anw))))
            
            
    return len(list(set(anw)))

  
  
  ##############
  
  
 ###에라토스테네스의 체.... 한수 배웁니다
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
