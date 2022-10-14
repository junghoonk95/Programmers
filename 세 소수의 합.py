import math
from itertools import*

def solution(n):
  cnt=0
  arr=[True for i in range(n+1)]
  arr[0]=False
  arr[1]=False
  for i in range(2,int(math.sqrt(n))+1):
      if arr[i]==True:
          j=2
          while i*j<=n:
              arr[i*j]=False
              j=j+1

  a=[i for i, p in enumerate(arr) if p]


  prime_sum=[sum(c) for c in list(combinations(a,3))]

  for i in prime_sum:
      if i==n:
          cnt=cnt+1
  return cnt

