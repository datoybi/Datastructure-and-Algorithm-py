
### ✔ 개발자의 소양
1. 추상화(상황 분석)
2. 절차적 사고
3. 구현 능력

    문제 -> 모델링(추상화) -> 절차적 사고 -> 구현

### ✔ 코테 대표 유형
- 파싱, 해싱, 정렬, 시뮬레이션 : 구현
- 탐색(BFS/DFS), 완전탐색(백트래킹) : 탐색
- 자료구조(스택, 큐, 힙) : 구조
- Greedy, DP, 이분탐색 : 알고리즘


<b> ❗ 문제를 분해하는 연습 필요 </b>
<br>

### ✔ 에러 종류

    a.컴파일 에러(CE) : 문법 오류
    (너무 많은 반복문을 돌거나 무한 루프에 빠지게 되었을 떄 발생 - 최적화를 하거나 조건문을 통해 반복문을 빨리 끊게 만든다)

    b. 시간 초과(TLE) : 최적화 필요 

    (메모리를 너무 많이 할당했을 떄 에러가 뜸)
    c. 메모리 초과(MLE) : 최적화 필요 

    (돌아가는 과정에서 오류가 생긴 경우. 답답함)
    d. 런타임에러(RE) : 과정 오류
        - 0으로 나누는 경우
        - Container에서 index 오류(접근)
        - 무한 루프 (TLE 이기도 함)

    e. 틀렸습니다(WA) : 수 많은 이유
        1. 제한 및 대소 관계 (이상, 이하, 초과, 미만, min, max) - 부등호 처리 잘해줬는지 확인
        2. 예외 처리 (단, 없는 경우는 -1을 출력한다~) - 주어진 예외처리를 잘했는지 확인
        3. 입력과 출력 (공백, 양식, 순서, 정렬 유무) - 
        4. 시간 제한과 메모리 제한 - 꼭확인
        5. 알고리즘이 맞는가? - 출제자가 원하는 알고리즘을 사용해야 한다
        6. 내가 생각한 로직대로 구현했나?
        7. 불필요한 반복문이 있는가?
        8. 중복은 처리했는가?

### ✔ 자주 묻는 질문들

    ❓ 문제 모델링이 어려워요
        - 수치 및 조건 정리하기 - 입력, 출력 변수 관리, 조건을 넘버링
            10명의 **값 정수로 주어잔다
                A = [int(input()) for i in range(10)]
            ~를 체크해야된다.
                def check(x):
                    pass
        - 전체적인 흐름 그리기 
        - a4나 아이패드에 흐름을 그리기
        - 입출력 예제 이해하기 

    ❓ 문제를 풀다가 자꾸 막혀요
        - 많이 푸는게 답
        - 필수 알고리즘은 암기하기(다다익선)
        - 설명과 함께 풀어보기 / 유형은 많이 풀기
        - 모델링을 바탕으로 기능을 가볍게 적어보기

    ❓ 풀이는 아는데 구현이 안된다
        - 디버깅 연습은 필수 -> 정답이 한번에 나오길 바라지 말자 , print로 디버깅하기
        - 쉽고 간단한 문제를 많이 풀자 - 알고리즘적 사고가 늘진 않지만, 조건문이나 기초 연산자 사용의 내공이 쌓임
        - 본인만의 스타일을 만들자
        - 연습에는 억지로 최적화 X 
        - 꼭 정해 풀이 알기 + 풀어보기

<b> ❗ 제일 중요한건 많이 푸는 것!!!!</b>

### ✔ 구현
    
- 프로그래밍의 기초 : 구현
	어떤 내용이 구체적인 사실로 나타나게 함 -> 문제 조건을 코드로 작성하여 돌아가게 함
	모든 프로그래밍 = 구현 문제

- 파이선 내장함수를 사용한 시뮬레이션
	내장함수만을 사용하면 기본적을 풀수 있다
	시뮬레이션 : 실제와 비슷한 모형을 만들어 실험하여 그 특성을 파악

- 코테에서 시뮬레이션이란?
	1. 문제 상황과 일대일 매칭
	2. 보다 효율적으로 짜는 것이 목표
	3. 최적화와 알고리즘 등 복잡한 코드까지

<br>
<b> ❗ 테크닉과 연습 필요 </b>   

### ✔ 파이썬 자료형의 기본 활용과 Tip

    ✔ 기본 자료형 
        - single : Integer, Float, String, Boolean
        - container : List, Tuple, Dictionary, Set

    ✔ Integer
     - 수의 크기 제한이 딱히 없음 -> overflow 걱정을 줄일 수 있음 
        print(2**1000) # 107150860718..... 

    - str()로 쉬운 형변환 
        print(str(123))

    - 연산/함수 사용 시, float로 변환되는 경우를 잘 살펴보자
        - 나눗셈은 /가 아닌 //로 안전하게 나누자(또는 divmod 사용)        
            print(3/3) # 1.0
            print(type(3/3)) # <class 'float'>
            print(type(3//3)) # <class 'int'>
            print(divmod(7,3)) # (2,1) 해가 2 나머지 1
            print(divmod(6,3)) # (2,0) 해가 2 나머지 0

    ✔ Float
        - 일단 연산에서는 쓰지 말자
            print(0.1 * 3 == 0.3) # false -> 실수의 오차 때문
        - 유리수 연산은?
            될 수 있다면 tuple 등으로 분자/분모를 따로 처리하자 
		    1/3 보다 (1,3), (2,3) 이런 형태로 저장
    
    ✔ String
        - immutable 변수 : 변경 불가능 
            a = "dasom" 
            for i in a:
                i = 'c'
            print(a) # dasom -> 변하지 않았다.

        - +연산과 *연산 조심하기
            s = 'abc'
            b = 'edf' 
            print(s+b) # abcedf -> 더하기는 가능
            print(s*3) # abcabcabc -> 더하기는 가능
    
        
	    - join() method 활용하기
            # case1
            s = ''
            for i in range(10000):
                s = s+str(i)

            # case2 
            s = ''
            s = s.join([str(i) for i in range(10000)])

            # case 1보다 2가 훨씬 빠르다. join을 되도록 사용하여서 시간초과를 방지하자

        -.split() .replace() 등 다양한 method 활용이 초점  
        - Slicing을 자유홉게 할 수 있는 것 
            s = 'abcd'
            print(s[:1]) # a

        - char를 ord와 chr로 다루기
            chr(65) # 'A'
	        ord('A') # 65

    ✔ boolean        
        - 논리 연산과 활용

        - Short Circuit
            if 0 and 1//0:	
                print('hello') # 런타임 에러가 아닌 이유는 앞의 항이 거짓이면 뒤의 항은 무시
            if 1 or 1//0:
                print('hello') # hello	앞의 항의 참이면 뒤의 항 무시

        - 모든 문제의 기본 : 참/거짓

    ✔ List
        - List Comprehension 사용하기     
            list_arr = [i for i in range(100)]
            set = ( i for i in range(1000))

        - sort와  sorted 구분하기
            lst = [3,5,6,9,2]
            print(sorted(lst)) # [2, 3, 5, 6, 9]
            print(lst)  # [3, 5, 6, 9, 2] lst는 정렬 안됨

            lst.sort() # 메서드
            print(lst) # [2, 3, 5, 6, 9] lst 자체를 정렬

        - 다양한 내장 함수 사용
            s = 'abs'
            lst = [3,5,6,9,2]

            print(len(s)) # 3
            print(len(lst)) # 5
            print(sum(lst)) # 25
            print(max(lst)) # 9
            print(min(lst)) # 2
            lst = [1] + lst	
            print(lst) # [1, 3, 5, 6, 9, 2]
    
        - slicing, [-1] 등 음수 인덱스 활용
            lst = [3,5,6,9,2]
            lst[:0]
            lst[-1]
            print(lst)

        - reduce, filter 도 활용하면 좋음 

    ✔ Tuple
        - 초기 상태 표현시 코드가 길어지는 것 방지   
            a,b,c = 1,2,3 # case1

            # case 2 
            a=1
            b=2
            c=3 
            # case1이 간결하다.
          
        - 동시에 변해야하는 객체에 효율적 표현 가능           
            a, b = 3, 7
            a, b = b, a
            print(a, b) 

    ✔ Dictionary     
        - keys나 value를 사용하여 효율적인 사용 추천 
            dic_test = {1:2, 2:3, 'abc':7}
            print(dic_test) # {1: 2, 2: 3, 'abc': 7}
            print(dic_test.values()) # dict_values([2, 3, 7])
            print(dic_test.keys()) # dict_keys([1, 2, 'abc'])

    ✔ Set
        - 중복 체크
            st = set([1,2,3,4,5,1,2,3,4,5,2,3,1])
            print(st) # {1, 2, 3, 4, 5}
            
            def isCheck(lst):
                return len(lst == len(set(lst))

        - 합집합, 여집합, 차집합 등 집합연산
            - 시간 복잡도가 크니 주의해서 사용             


