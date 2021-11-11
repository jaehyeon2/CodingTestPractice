def solution(s):
    answer = len(s)
    for length in range(1, len(s)//2+1):
        compressed=""
        prev=s[0:length]
        count=1
        for j in range(length, len(s), length):
            if prev==s[j:j+length]:
                count+=1
            else:
                if count>=2:
                    compressed+=str(count)+prev
                else:
                    compressed+=prev
                prev=s[j:j+length]
                count=1
        if count>=2:
            compressed+=str(count)+prev
        else:
            compressed+=prev
        answer=min(answer, len(compressed))
        
    return answer

#p.323 문자열 압축