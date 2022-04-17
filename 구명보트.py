from collections import*
def solution(people, limit):
    peoples = deque(sorted(people.copy()))
    cnt = 0
    
    while len(peoples) >1:
        if peoples[0] + peoples[-1] <= limit:
            peoples.popleft()
            peoples.pop()
            cnt=cnt+1
        else:
            peoples.pop()
            
    return len(people)-cnt


### 50 70 80
# 50 50 70 80


`
########################
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
