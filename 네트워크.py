
def dfs(idx,n,visit,target):
    visit[idx]=True
    for j in range(n):
        if idx!=j and target[idx][j]==1:
            if visit[j]==False:
                dfs(j,n,visit,target)


def solution(numbers, target):
    visit=[False for _ in range(numbers)]
    cnt=0

    for i in range(numbers):
        if visit[i]==False:
            dfs(i,numbers,visit,target)
            cnt=cnt+1
    return cnt




