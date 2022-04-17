def solution(n, words):
    cnt=0
    word=[]
    word.append(words[0])
    for i in range(1,len(words)):
        if word[i-1][-1] ==words[i][0] and words[i] not in word:
            word.append(words[i])
            cnt=cnt+1
        else:
            
            break
            
    if word== words:
        return [0,0]
    else:
        return[1+(cnt+1)%n ,(cnt+1)//n+1]
    # return cnt, word
    
    
    
#################

def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
