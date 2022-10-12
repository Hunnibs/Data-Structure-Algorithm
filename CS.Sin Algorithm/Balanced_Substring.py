'''
최대 길이의 균형 부문자열
0과 1이 섞여 있는 문자열에서 i < j에 대해, A[i]부터 A[j]까지의 부문자열에서 0과 1의 개수가 같다면 균형 부문자열(balanced substring)이라 정의한다.
'''

'''
자료구조 중 해시테이블을 활용하였다. 문자열을 돌며 0과 1의 개수를 차례대로 카운트 해줘서 개수의 차이를 기준으로 해시함수를 사용한다.
시간은 총 O(n)만큼이 소요된다. 
'''

def solve(A):
    cnt0 = 0
    cnt1 = 0
    result = 0

    D = dict()  # 해시테이블로 활용할 Dict 
    D[0] = -1   # 인덱스가 0부터 시작하기 때문

    for i in range(len(A)):
        if A[i] == '0':
            cnt0 += 1
        else:
            cnt1 += 1

        if D.get(cnt1 - cnt0) == None: 
            D[cnt1-cnt0] = i  
        else:
            result = max(result, i - D[cnt1-cnt0])
    
    return result

A = input().strip()
print(solve(A))