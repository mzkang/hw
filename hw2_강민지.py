# Assignment Number...: 2
# Student Name........: 강민지
# File Name...........: hw2_강민지
# Program Description : 문자열 자료형의 변수를 생성하고 슬라이싱하는 과제입니다.



cellphone = 'Samsung Galaxy7'  # cellphone이라는 변수를 만들어 'Samsung Galaxy7'이라는 문자열을 저장한다.
print(cellphone)   # cellphone 변수를 출력하기 위해 print 함수를 사용했다.


company = cellphone[0:7]  # cellphone이라는 문자열 변수를 slicing하여 'Samsung'이라는 문자열을 추출한다.
                          # slicing은 [첫문자번호:끝문자번호+1]인데, 'Samsung'은 0~6자리 숫자이므로 [0:7]로 slicing한다.
                          # 그리고나서 company라는 변수를 만들어 'Samsung'이라는 추출된 문자열을 저장한다.
print(company)  # company 변수를 출력하기 위해 print 함수를 사용했다.
model = cellphone[8:len(cellphone)]   # cellphone이라는 문자열 변수를 slicing하여 'Galaxy7'이라는 문자열을 추출한다.
                                      # slicing은 [첫문자번호:끝문자번호+1]로 하는데,
                                      # 'Galaxy7'은 8~문자열길이-1이므로 [8:len(cellphone)]으로 slicing한다.
                                      # 그리고나서 model이라는 변수를 만들어 'Galaxy7'이라는 추출된 문자열을 저장한다.


print(model)   # model 변수를 출력하기 위헤 print 함수를 사용했다.
print(type(company))   # company 변수의 자료형을 확인하기 위해 type 함수를 사용했고, 그 결과를 출력하는 데에 print 함수를 사용했다.
print(type(model))     # model 변수의 자료형을 확인하기 위해 type 함수를 사용했고, 그 결과를 출력하는 데에 print 함수를 사용했다.


print('It had been that way for days and days.\n\
 And then, just before the lunch bell rang, he walked into our class room.\n\
 Stepped through that door white and softly as the snow.')   # 문자열이므로 ''로 묶었고, 결과 출력을 위해 print 함수를 사용했다.
                                                      # 각 문장마다 줄바꿈을 해줬으므로 이스케이프 부호 \n을 줄바꾸는 곳에 사용했다.
                                                      # 그리고 문장이 너무 길어서 \를 사용하여 여러 줄에 나눠 작성했다.

