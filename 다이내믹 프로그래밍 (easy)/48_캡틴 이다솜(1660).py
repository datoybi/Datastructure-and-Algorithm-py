# 문제를 이해못하겠다
# 아 이해했다

'''
맞았습니다!!
처음에는 문제 이해를 잘 못했었는데 나중에 혼자힘으로 푼 문제!! 뿌듯

사면체 숫자들을 나열하면 1, 4, 10, 20, 35, 56, 84..가 되는데,
79 = 35 + 20 + 20 + 4 로 4가 답입니다.
하지만 sanghwaann님의 방법으로는 79 = 35 + 35 + 4 + 4 + 1 이 되어 4의 답을 찾아내지 못합니다.

'''

n = int(input())
dp1 = [125] * (n+3)
dp1[0] = 0; dp1[1] = 1; dp1[2] = 4

for i in range(3, n+1): # 대포알 계산
    dp1[i] = dp1[i-1] * 2 - dp1[i-2] + i
# print(dp1)

dp2 = [99999999] * (n+3)
dp2[0] = 0; dp2[1] = 1; dp2[2] = 2;

for i in range(3, n+1):
    for j in range(1, len(dp1)):
        if dp1[j] <= i:
            dp2[i] = min(dp2[i], dp2[i-dp1[j]]) 
        if dp1[j] > i: break
    dp2[i] += 1

print(dp2[n])
