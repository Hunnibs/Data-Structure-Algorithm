'''
x-축 위에 n개의 점 집합 p가 입력으로 주어지고, 각 점은 1번부터 k번 중 하나의 색으로 칠해져 있다.
연속된 구간의 점으로 구성된 부분 집합 p'를 고려해보자. p의 점들에 대해, 1번부터 k번 색이 최소 한 번 이상 등장하면 p'를 무지개라 부른다.
p-p' 역시 1번부터 k번 색이 최소 한 번 이상 등장하면 p-p' 역시 무지개가 된다.
만약 p'과 p-p' 모두 무지개라면 이를 쌍 무지개라고 부른다.
여러 개의 쌍 무지개가 존재할 수 있다. 그 중에서 |p'|이 제일 작은 쌍 무지개를 찾아 |p'|을 출력하는 프로그램을 구현해보자

입력:
첫 줄에 두 자연수 n과 K 값이 차례로 주어진다.
다음 n개의 줄에는 각 점의 색 번호가 주어진다. i번째 줄의 자연수

출력:
쌍 무지개가 되는 최소 |p'|을 출력한다. 
'''

'''
처음시작할때 전체를 P'으로 생각한다. 이후 while문을 돌면서 P'에서 제외된 색깔은 P에 포함된 색깔로 업데이트 해준다. 이렇게 반복문을 돌면서 가장 최소구간에서 조건을 만족하는 경우를 마지막에 출력해주는 방식을 사용
시간복잡도는 While문 하나를 도는데 최악의 경우 O(n) 나머지 초기화 시키는데도 O(n)씩 걸린다 전체 시간복잡도가 Kn이므로 총 O(n)시간으로 볼 수 있다. 
'''

from cmath import inf

def rainbow(A, c1, c2, n, k):
    p = 0  # p에 포함된 색깔 개수
    p2 = k  # p'에 포함된 색깔 개수

    left, right = 1, 0  # p' range
    min = inf

    while left <= n and right <= n:
        if p != k:  # p' 범위 증가
            right += 1
            if right > n-1:  # 인덱스의 끝에 도달할 경우
                break;
            
            c2[A[right]] -= 1  # p'에서 나온 색깔을 카운팅에서 빼줌
            
            if c2[A[right]] == 0:
                p2 -= 1
            if c1[A[right]] == 0:
                p += 1
            
            c1[A[right]] += 1  # P의 해당 색깔 counting
        
        else:
            if p2 == k:
                size = right - left + 1
                if size < min:
                    min = size

            left += 1
            if left > right:  # p'의 left가 right보다 더 넘어갈 경우
                break

            c1[A[left-1]] -= 1  # p에서 나온 색깔을 카운팅에서 빼줌
            
            if c1[A[left-1]] == 0:
                p -= 1
            if c2[A[left-1]] == 0:
                p2 += 1
            
            c2[A[left-1]] += 1  # p'의 해당 색깔 counting


    if min == inf:
        return 0
    else:
        return min


# main
n, k = map(int, input().split())
A, c1, c2 = [], [], []

#init
for i in range(k+1):
    c1.append(0)  # p의 색깔 카운팅
    c2.append(0)  # p'의 색깔 카운팅

for i in range(n):  
    num = int(input())
    A.append(num)  # 입력값 리스트
    c2[num] += 1  # 초기 P'의 색깔 카운팅

print(rainbow(A, c1, c2, n, k))