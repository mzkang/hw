# Assignment Number...: 8
# Student Name........: 강민지
# File Name...........: hw8
# Program Description : 패키지와 모듈을 불러오고 함수를 정의하고 활용하는 과제입니다.



from datetime import *   # datetime.now 함수를 사용하기 위해서 datetime 모듈을 불러왔다. 

now = datetime.now()     # 현재 시간을 저장하기 위해 datetime.now() 함수를 사용해서 now 변수에 저장했다.
print(now.strftime('%Y-%m-%d %H:%M:%S')) # now 변수를 원하는 형식으로 정의하기 위해 now.strftime 함수를 사용했고
                                         # print로 결과를 출력했다. 




from calendar import *    # calendar 모듈에 들어있는 함수를 사용하기 위해서 calendar 모듈을 불러왔다.

print(isleap(2050))       # 2050년이 윤년인지 아닌지 확인하는 함수 isleap를 사용하고 print로 결과를 출력했다.
print(weekday(2050,7,7))  # 2050년 7월 7일이 어떤 요일인지 알려주는 함수 weekday를 사용하고 print로 결과를 출력했다.




from collections import *  # collections의 Counter을 사용하기 위해 collection 모듈을 모두 불러왔다.

def vowel(s):              # 매개변수가 문장 s인 함수 vowel을 정의했다.
    counts = Counter(s.lower())  # 대소문자 구별을 없애기 위해 lower로 문장s를 모두 소문자로 바꾸고, Counter 함수로 각 문자 개수를 셌다. 
    mo = {}                # 문장 s에 들어있는 문자 중 모음만 선택해서 그 갯수를 세서 넣을 빈 딕셔너리를 만들었다.
    for k in ['a','e','i','o','u']:  # 모음을 하나씩 뽑아서 순환문을 돌린다.
        mo[k] = counts[k]            # mo 딕셔너리에 value를 counts[k](문장 s의 k개수)로 하는 k(모음)라는 키를 만들어 추가했다.
        print('The number of ' + k + ': ' + str(counts[k])) # k의 개수를 알려주는 문장을 print로 출력했다.
                                                            # +로 연결했으므로 count[k]를 str로 변환했다.
    mo = mo.items()   # mo.items 함수로 mo 딕셔너리 안의 key와 value를 key:value에서 (key, value) 형태로 바꿨다.
    mo = sorted(mo, key = lambda e : (e[1]), reverse = True) # 제일 많이 나온 모음을 찾기 위해 sorted 함수로 정렬했다.
    # 그 과정에서 value 값을 비교하기 위해 람다함수를 사용했고, value를 기준으로 내림차순 정렬을 하려고 reverse=True를 했다. 
    mx = mo[0][0] # 제일 많이 나온 모음을 뽑아내기 위해, 내림차순 정렬된 mo에서 첫번째 위치의 값을 뽑으려고 mo[0]을 했다.
                  # 또, (k, counts[k])에서 모음은 첫번째 위치이므로 제일 많이 나온 모음을 mo[0][0]으로 뽑아 변수 mx에  저장했다.
    print(s.replace(mx, mx.upper())) # 문장s에서 mx를 대문자로 바꿔주기 위해 replace 함수를 사용했고 print로 출력했다.

vowel('The regret after not doing something is bigger than that of doing something.')   # 문자열을 넣어 함수를 실행했다.
   
