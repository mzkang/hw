
#============??????????????????????return.....??????????????????/=============================

def count(n):
    if n > 0 :
        print(n)
        return count(n-1)
    else :
        return 'zero!!'
    
x = count(5)
print()
print(x)
#=============================================================================================
    
# Assignment Number...: 6
# Student Name........: 강민지
# File Name...........: hw6
# Program Description : 새로운 함수를 정의하고, 람다함수를 익히는 과제입니다.


def area_triangle(h, w):  # 두 개의 인수 h(삼각형의 높이),w(밑변의 길이)를 받는 함수 area_triangle을 def로 정의했다.
    return 0.5 * h * w    # return을 사용하여 결과값으로 삼각형의 면적(0.5 * h * w)를 돌려준다.
print(area_triangle(10,15)) # area_triangle 함수에 h=10, w=15를 순서대로 입력하고 print 함수로 결과를 출력했다.



def distance(a,b):          # 두 개의 인수 a,b를 받는 함수 distance를 def로 정의했다.
    result = 0              # 각 차원에 해당하는 좌표 차의 제곱을 구해서 더한 값을 저장하기 위해 result 변수를 만들고 0으로 설정했다.
    for i in range(len(a)): # 좌표의 차원이 len(a)이므로 차원만큼 루프를 돌려준다.
        result += (a[i] - b[i])**2   # 각 차원에 해당하는 좌표 차의 제곱을 구해서 result에 더해준다.
    return result ** 0.5    # 루프가 다 돌아가면 위의 결과에 루트를 취하기 위해서 0.5제곱을 해준다.
print(distance((1,2),(5,7))) # distance 함수에 a=(1,2), b=(5,7)을 순서대로 입력하고 print 함수로 결과를 출력했다. 




    
def count(n):      # 하나의 인수 n을 갖는 count 함수를 def로 정의했다.
    if n > 0 :     # n>0 이면 print 함수로 n을 출력하고 count(n-1)을 호출하는 if문을 만들었다.
        print(n)
        count(n-1)
    else :         # n이 1씩 작아지다가 0이 되면 위의 조건을 만족하지 않으므로 그 경우를 else라 했다.
        print('zero!!')  # print 함수로 zero!!를 출력했다.
count(5)    # count 함수에 n=5를 입력하고 결과를 출력했다.
            # 여기에서 print를 쓰지 않은 이유는 함수에 print가 있어서 또 print를 하면 None이 출력되기 때문이다.

    

area_triangle_ld = lambda h, w: 0.5 * h * w  # <lambda 매개변수 : 표현식>이므로 매개변수 자리에 h,w를 넣고 표현식에 삼각형의 면적을 넣었다.
print(area_triangle_ld(10,15))    # area_triangle_ld 함수에 h=10, w=15를 순서대로 입력하고 print 함수로 결과를 출력했다.

