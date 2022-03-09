
def solution(array, commands):
    answer = []
    for i in commands:
        
        answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    
    return answer
  
  
  

  
```
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
  
  
```

#모범답안


def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

#map, lamda
