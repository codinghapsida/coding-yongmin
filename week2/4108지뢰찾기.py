import sys
while 1:        # 무한반복
    str = []        # 입력받을 배열
    R, C = map(int, input().split()) # 행, 열 입력 받음
    if R==0 or C==0: # 0 0 들어오면 종료
        break
    
    for _ in range(R): 
        str.append(sys.stdin.readline().strip()) # 한 줄씩 읽는데 뒤에 개행문자 제거하려고 strip()

    for i in range(R):      
        for j in range(C):      # 문자 개수만큼 (행열 크기만큼) 반복
            if str[i][j] == '.': # 지뢰가 아닌지 확인
                count = 0       # 지뢰 개수 셀 변수
                for k in range(-1, 2, 1): # 주변 여덟칸 탐색
                    for l in range(-1, 2, 1): # 주변 여덟칸 탐색
                        if (i+k)>=0 and (j+l)>=0 and (i+k)<R and (j+l)<C: # 범위 이탈하지 않도록
                            if str[i+k][j+l] == '*': count+=1 # 지뢰 찾으면 카운트
                print(count, end = '') # 지뢰 개수 출력
            else: print('*', end = '') # 애초에 지뢰였으면 그대로 지뢰 출력
        print() # 개행