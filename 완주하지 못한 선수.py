#1st Try

def solution(participant, completion):
    par=sorted(participant.copy())
    com=sorted(completion.copy())
    for i in par:
        if i in com:
            com.remove(i)
        else:
            return(i)

```
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.22ms, 10.3MB)
테스트 4 〉	통과 (0.49ms, 10.4MB)
테스트 5 〉	통과 (0.45ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (40.82ms, 18.3MB)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	통과 (219.05ms, 26.7MB)
```

#2nd try
