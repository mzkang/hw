# Assignment Number...: 4
# Student Name........: 강민지
# File Name...........: hw4
# Program Description : 제어문(조건문, 반복문)을 활용하는 과제입니다.




restaurant_list = [{'상호':'A','메뉴':'피자','가격(원)':20000},    # 식당목록표를 참고하여 각 식당마다 dict자료형으로 이루어진 
                   {'상호':'B','메뉴':'치킨','가격(원)':18000},    # list자료형으로 만들어, 변수 restaurant_list에 저장했다.
                   {'상호':'C','메뉴':'짜장면','가격(원)':5000},   # '가격(원)' key에 해당하는 values는 int라서 따옴표가 없고
                   {'상호':'D','메뉴':'초밥','가격(원)':15000},    # 나머지 key에 해당하는 values는 str이라 따옴표로 묶었다. 
                   {'상호':'E','메뉴':'치킨','가격(원)':23000},    
                   {'상호':'F','메뉴':'족발','가격(원)':30000}]

want_to_eat = input('먹고 싶은 음식을 입력하세요 : ')  # input 함수를 사용해 먹고 싶은 음식을 입력받아, want_to_eat에 str로 저장한다.





index = 0      # 반복문을 사용하기 위해 index를 0으로 만들었다.
x= []          # want_to_eat에 저장된 메뉴가 restaruant_list 안의 dict에 존재하면, x에 그 메뉴를 넣기 위해 빈 리스트를 생성했다. 
while index < len(restaurant_list):  # 식당의 개수가 바뀔 수 있으므로 길이를 지정하지 않고 len 함수를 사용했다. 
    if want_to_eat == restaurant_list[index]['메뉴']:  # want_to_eat과 각 식당의 메뉴가 같은지 확인한다. 
        x += [want_to_eat]                             # want_to_eat과 메뉴가 같은 식당이 나타나면 그 메뉴를 리스트 x에 추가한다.
        print('식당{}, 가격{}원'.                      # want_to_eat과 메뉴가 같은 식당과 가격을 출력하기 위해 print 함수를 사용했다.
              format(restaurant_list[index]['상호'],
                     restaurant_list[index]['가격(원)']))
    index += 1  # 다음 식당을 확인하기 위해 index를 1씩 늘려간다.
else:         
    if len(x) == 0:  # x의 길이가 0이라는 것은 x에 아무것도 들어있지 않은 빈 리스트라는 의미이다.
                     # x에 아무것도 들어있지 않다는 것은 want_to_eat의 메뉴와 일치하는 식당이 없다는 뜻이다.
        print('결과값이 없습니다') # 결과를 출력하기 위해 print 함수를 사용했다.

        
        
        
        
#===================================================================================================================================

# 100점 다미 코드

# 3. 입력 받은 음식을 파는 식당이 restaurant_list에 있는지 확인 후 적절한 메시지를 출력하도록 설계한다.
# 3-1) food_found 초기 설정: False
food_found = False
# 3-2) list의 모든 항목에 대해 수행하도록 list 길이만큼의 for 반복문 설정
for i in range(len(restaurant_list)):
    # 3-3) list의 i번째 항목(i.e. 각 dict 자료)에서 key가 ‘메뉴’인 요소의 값 중 입력 받은 음식과 같은 것 있는지 검색
    if want_to_eat in restaurant_list[i]['메뉴']:
        # 3-4) 동일 항목이 존재하는 경우, dict의 ‘상호’, ‘가격’ 항목의 값을 활용하여 '식당 X, 가격 Y원' 메시지 출력
        print('식당 {}, 가격 {} 원'.format(restaurant_list[i]['상호'], restaurant_list[i]['가격']))
        # 3-5) list 내 동일 항목이 존재하는 경우, 기본 값이 False였던 food_found를 True로 변경
        food_found = True
# 3-6) food_found가 False인 경우(i.e. 입력 받은 음식이 list 내에 존재하지 않는 경우) '결과가 없습니다' 메시지 출력
if not food_found:
    print('결과가 없습니다.')

