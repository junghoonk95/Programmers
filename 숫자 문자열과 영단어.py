def solution(s):
    letter=["zero","one","two","three","four","five","six","seven","eight","nine"]
    num=[0,1,2,3,4,5,6,7,8,9]


    for i in range(10):
        if str(letter[i]) in s:
            s=s.replace(letter[i],str(num[i]))

    return int(s)
  
  
  
  ## best 풀이
  

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
