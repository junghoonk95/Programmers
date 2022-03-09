  def solution(answers):

    b = []
    a = [[1, 2, 3, 4, 5] * 2000, [2, 1, 2, 3, 2, 4, 2, 5] * 2000, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2000]
    c=[]
    for i in a:
        cnt = 0
        for p, a in zip(answers, i):
            if p==a:
                cnt=cnt+1
        b.append(cnt)


    for j in range(3):
        if max(b)==b[j]:
            c.append(j+1)

    return c

  ```
  정확성  테스트
테스트 1 〉	통과 (0.26ms, 10.4MB)
테스트 2 〉	통과 (0.26ms, 10.3MB)
테스트 3 〉	통과 (0.27ms, 10.4MB)
테스트 4 〉	통과 (0.40ms, 10.3MB)
테스트 5 〉	통과 (0.28ms, 10.4MB)
테스트 6 〉	통과 (0.39ms, 10.3MB)
테스트 7 〉	통과 (1.25ms, 10.3MB)
테스트 8 〉	통과 (0.72ms, 10.4MB)
테스트 9 〉	통과 (1.42ms, 10.4MB)
테스트 10 〉	통과 (1.43ms, 10.3MB)
테스트 11 〉	통과 (2.75ms, 10.5MB)
테스트 12 〉	통과 (1.46ms, 10.4MB)
테스트 13 〉	통과 (0.49ms, 10.3MB)
테스트 14 〉	통과 (1.63ms, 10.4MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0

```

#모범답안



def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
