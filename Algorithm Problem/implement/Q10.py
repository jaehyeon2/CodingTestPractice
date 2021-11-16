def rotate_key(key):
    n=len(key)
    result=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-i-1]=key[i][j]
    return result
    
def clear(lock):
    length=len(lock)//3
    for i in range(length, length*2):
        for j in range(length, length*2):
            if lock[i][j]!=1:
                return False
    return True
        
    
def solution(key, lock):
    n=len(lock)
    m=len(key)
    new_lock=[[0]*(3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]
    
    for rotation in range(4):
        key=rotate_key(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                if clear(new_lock)==True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]
    
    return False

#p.325 자물쇠와 열쇠