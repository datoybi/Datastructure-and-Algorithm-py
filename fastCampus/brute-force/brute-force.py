'''
완전 탐색
    문제를 해결하기 위해 확인해야 하는 모든 경우를 전부 탐색하는 방법
    그 중에서도 백 트래킹(Back-Tracking)을 통해야 하는 상황을 해결하기!
    모든 코테 문제에서 기본적으로 접근해 봐야 한다. 많은 연습이 필요!

    GOOD : 부분 점수를 얻기 좋다.
    BAD : 전부 탐색하기에 시간 복잡도가 일반적으로 높다.

    코테에 나오는 완전 탐색 종류 4가지
        N개 중 - 중복을 하용해서, 중복없이
        M개를 순서있게 나열하기, 고르기
'''
'''
    완전탐색은 함수의 정의가 50% 먹고 들어간다.
    # Recurrence Function (재귀 함수)
    만약 M개를 전부 고름 => 조건에 맞는 탐색을 한 가지 성공한 것!
    아직 M개를 고르지 않음 => k번째부터 M번째 원소를 조건에 맞게 고르는 모든 방법을 시도한다. (?)

    def rec_func(k):
        ...

    input()
    rec_func(1) # 1번째 원소부터 M번째 원소를 조건에 맞게 고르는 모든 방법을 탐색해줘
    print(sb)
    
    백트래킹은 재귀함수의 정의가 중요
'''