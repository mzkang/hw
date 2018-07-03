# Assignment Number...: 5
# Student Name........: 강민지
# File Name...........: hw5
# Program Description : if-else문과 for,while문을 활용하는 과제입니다.


a= int(input('Enter a: '))  # input 함수를 이용하여 입력받은 값에 int 함수를 사용하여 정수를 만들었다. 
b= int(input('Enter b: '))  # 그리고 그 정수를 변수 a,b,c에 각각 저장했다.
c= int(input('Enter c: '))

if a > b and a > c :        # a가 b와 c보다 동시에 커야하므로 and를 사용했다. 
    print(b+c)              # 조건을 만족했을 때 b+c를 출력하기 위해 print 함수를 사용했다.
elif b > a and b > c :      # 위의 조건을 만족하지 않는 경우, b가 a와 c보다 동시에 큰지 확인한다. 
    print(a+c)              # 조건을 만족했을 때 a+c를 출력하기 위해 print 함수를 사용했다.
elif c > a and c > b :      # 위의 두 조건을 만족하지 않는 경우, c가 a와 b보다 동시에 큰지 확인한다.  
    print(a+b)              # 마지막에 else가 아니라 elif인 이유는 만족해야할 조건이 있기 때문이다.
                            # 조건을 만족했을 때 a+b를 출력하기 위해 print 함수를 사용했다.



city = input('Enter the name of the city: ') # input 함수를 이용해 도시를 입력 받아 city라는 변수에 저장했다. 

if city == 'Seoul' :      # city가 Seoul이라는 조건을 만족하는지 확인하기 위해 ==를 사용했다. =는 변수를 저장하는 것.
    size = 605            # 조건을 만족하면 size가 605가 된다.     
elif city == 'New York' : # 위의 조건을 만족하지 않는 경우, city가 New York인지 확인한다.
    size = 789            # 조건을 만족하면 size가 789가 된다.
elif city == 'Beijing' :  # 위의 조건을 만족하지 않는 경우, city가 Beijing인지 확인한다.
    size = 16808          # 조건을 만족하면 size가 16808이 된다.
else:                     # 위의 조건을 모두 만족하지 않는 나머지의 경우
    size = 'Unknown'      # size가 Unknown이 된다. Unknown은 문자열이므로 '' 안에 쓴다.
print('The size of {} is {}'.format(city, size))    # format 함수를 이용하여 주어진 형식의 문자열을 만들었다.
                                                    # print를 이용하여 문자열을 출력했다.



import math                  # math 라이브러리를 불러왔다.
for i in range(10):          # range(k)는 0부터 k-1까지 정수를 차례로 출력하므로 k=10을 넣어 for문을 만든다. 즉, 0~9까지 반복하게 된다.
    print(math.factorial(i)) # print 함수를 사용하여 계승값(factorial)을 계산해서 차례대로 출력한다.
    
    


index = 0                           # while문을 위해 index를 설정한다. 0의 계승값부터 구하기 때문에 0에서 시작했다.
while index < 10:                   # 0~9까지 정수의 계승값을 구할 것이라서 10보다 작다는 조건을 줬다. 0부터 시작한다.
    print(math.factorial(index))    # print 함수를 사용하여 계승값(factorial)을 계산해서 차례대로 출력한다.
    index += 1                      # index를 1씩 늘려준다. 
