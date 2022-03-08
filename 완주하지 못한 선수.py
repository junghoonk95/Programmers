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


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant,completion):
        if p!=c:
            return p
        
    return participant.pop()


```
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.19ms, 10.2MB)
테스트 4 〉	통과 (0.41ms, 10.2MB)
테스트 5 〉	통과 (0.39ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (33.91ms, 17.9MB)
테스트 2 〉	통과 (58.74ms, 22.1MB)
테스트 3 〉	통과 (64.54ms, 24.7MB)
테스트 4 〉	통과 (76.56ms, 26.3MB)
테스트 5 〉	통과 (75.47ms, 26.2MB)

```

# Best solution

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

