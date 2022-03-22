import re
def solution(a):
    a=a.lower()
    a=re.sub(r'[^\d|\w|\-|_|.]','',a)
    a=re.sub(r'^[.]{1,}|[.]{1,}$','',a)
    a=re.sub(r'[.]{2,}','.',a)
    
    if a =='':
        a="a"
    a=a[:15]

    if len(a)==0:
        a="aaa"
    if len(a)==1:
        a=a*3
    if len(a)==2:
        a=a+a[-1]
    a=re.sub(r'^[.]{1,}|[.]{1,}$','',a)
    a=re.sub(r'[.]{2,}','.',a)
    return a
  
  
  ###모범 답안 ,같은 정규식 다른느낌 
  
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
