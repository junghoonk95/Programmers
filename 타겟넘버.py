def solution(numbers, target):

    ans=0
    cnt=0
    def dfs(index,result):
        if index==len(numbers):
            if target==result:
                nonlocal cnt
                cnt=cnt+1
            return
        else:
            dfs(index+1,result+numbers[index])
            dfs(index+1,result-numbers[index])

    dfs(0,0)
    return cnt

print(solution([4,1,2,1],2))



#  개쩌는 풀이법1

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

#2
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
