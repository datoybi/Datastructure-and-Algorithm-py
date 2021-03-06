'''
    3가지 종류의 우유를 섞기로 함
    a에서 b에 부을때, 그는 a가 거의 비어질때까지 부을것이다.
    
    100번 붓고 나면 각각의 버킷엔 어떻게 차있을 까

    용량 : C 우유의 양 3 X3개


A_Capacity, A_Amount = map(int,input().split(' '))
B_Capacity, B_Amount = map(int,input().split(' '))
C_Capacity, C_Amount = map(int,input().split(' '))

# print(A_Capacity, A_Amount)
count = 0
selected = 'A'

while(count <= 4):
    if selected == 'A':
        if B_Capacity < A_Amount + B_Amount:
            A_Amount = A_Amount + B_Amount - B_Capacity
            B_Amount = B_Capacity
            count += 1
        else:
            B_Amount = A_Amount + B_Amount
            A_Amount = 0
            count += 1
        selected = 'B'
        if(count <= 4): 
            break
    print(A_Amount , B_Amount , C_Amount, count)

    if selected == 'B':
        if C_Capacity < B_Amount + C_Amount:
            B_Amount = B_Amount + C_Amount - C_Capacity
            C_Amount = C_Capacity
            count += 1
        else:
            C_Amount = B_Amount + C_Amount
            B_Amount = 0
            count += 1
        selected = 'C'
        if(count <= 4): 
            break
    print(A_Amount , B_Amount , C_Amount, count)

    if selected == 'C':
        if A_Capacity < C_Amount + A_Amount:
            C_Amount = C_Amount + A_Amount - A_Capacity
            A_Amount = A_Capacity
            count += 1
        else:
            A_Amount = C_Amount + A_Amount
            C_Amount = 0
            count += 1
        selected = 'A'
        if(count <= 4): 
            break
    print(A_Amount , B_Amount , C_Amount, count)

print(A_Amount , B_Amount , C_Amount, count)

'''

# 강사코드

C, M = list(), list()
# 우유와 용량을 따로 관리 -> 가독성을 높임 
for i in range(3):
    a, b = map(int, input().split())
    C.append(a)
    M.append(b)

for i in range(100):
    idx = i % 3 # 0, 1, 2
    nxt = (idx + 1) % 3
    M[idx], M[nxt] = max(M[idx] - (C[nxt] - M[nxt]), 0), min(C[nxt], M[nxt] + M[idx]) # 다 주거나 남으면 이만큼 남음

for i in M:
    print(i)
