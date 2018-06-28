# Assignment Number...: 3
# Student Name........: 강민지
# File Name...........: hw3
# Program Description : 문자열 서식을 활용하고, 리스트와 튜플을 생성하여 슬라이싱하는 과제입니다.





print('스테이크의 원래 가격은 {price}원입니다. \
하지만 VAT가 {VAT}로, 계산하셔야 할 가격은 {total}원입니다.\
'.format(price = 30000, VAT = '15%',       # price, VAT, total 키워드와 format함수를 활용하여 주어진 형식의 문자열을 만들었다.
         total = int(30000 + 30000*0.15))) # VAT이 반영된 실제 가격은 스테이크 가격 + 스테이크 가격 * VAT으로 계산했다.
                                           # 문자열을 출력하기 위해 print 함수를 사용했다.




s='@^TrEat EvEryonE yOu meet likE you want tO be treated.$%'  # 변수 s를 만들어 주어진 문자열을 저장했다.
print(s[2:-2].capitalize())      # 특수 문자를 없애기 위해서 문자열  slicing을 사용했다.
                                 # slicing은 [첫문자번호:끝문자번호+1] 로 하는데,
                                 # 문자열을 시작하는 T는 2번 자리, 문자열이 끝나는 .은 -3번 자리 이므로 [2:-3+1]로 slicing 했다.
                                 # 그리고나서 맨 처음 문자만 대문자로 만들기 위해 capitalize 함수를 사용했다.
                       # slicing을 먼저 한 이유는, capitalize를 먼저 하면 첫번째 문자가 @가 되므로 T는 t로 쓰이게 되기 때문이다.






numbers = 2,18,26,89,45,39,14  # 변수 numbers를 만들어 주어진 튜플을 저장했다. 튜플은 ()를 생략할 수 있다.
print(numbers)    # numbers 변수를 출력하기 위해 print 함수를 사용했다.




print(len(numbers))  # len 함수를 사용하여 튜플인 변수 numbers의 요소의 개수를 확인한다.
                     # numbers의 요소 개수를 출력하기 위해 print 함수를 사용했다.






fruits = list({'apple','orange','strawberry','pear','kiwi'})  # 변수 fruits를 만들어 주어진 집합의 원소를 요소로 갖는 list를 저장했다.
print(fruits)  # 변수 fruit을 출력하기 위해 print 함수를 사용했다.




fruits_sub = fruits[:3]  # 처음 세 요소만으로 이루어진 리스트를 만들기 위해 list를 slicing한다.
                         # 3번째 요소는 2번 자리이므로 [:2+1]로 slicing 했다.
print(fruits_sub)        # 변수 fruits_sub를 출력하기 위해 print 함수를 사용했다.


