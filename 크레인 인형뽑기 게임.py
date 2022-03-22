def solution(board, moves):

    arr = [[] for _ in range(len(board))]
    answer = []
    cnt=0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0 or board[i][j]:
                arr[j].append(board[i][j])
    for i in moves:
        if arr[i-1] != []:
            x=arr[i-1].pop(0)
            answer.append(x)


    def remo(answer):
        nonlocal cnt
        for i in range(len(answer)-1):

            if answer[i] == answer[i+1]:
                answer.pop(i)
                answer.pop(i)
                cnt=cnt+1
                remo(answer)
                return 
        return answer
    
    remo(answer)


    return cnt*2

### 모범답안 젠장 이렇게 간단...

def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
