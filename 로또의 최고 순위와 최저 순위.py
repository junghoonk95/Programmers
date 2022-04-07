def solution(lottos, win_nums):
    cnt=0
    zero=0
    answer = []
    for i in lottos:
        if i in win_nums:
            cnt=cnt+1
        if i == 0:
            zero=zero+1

    if cnt==1 :
        cnt=1
    if cnt==0:
        cnt=1
        if zero>0:
            zero=zero-1

    return [7-cnt-zero,7-cnt]
  
  
  
  ------------------------------------
  #모범답안

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
