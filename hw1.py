season = input('What is your favorite season? ') 
print(season)       #season 변수를 출력하기 위해 print를 사용        
date = input('Which date were you born? ')
print(type(date))   #type으로 date의 자료형을 확인하고, 그 결과를 print로 출력
date = float(date)  #date 변수 자료형을 float으로 변경
print(type(date))   #type으로 date의 자료형을 확인하고, 그 결과를 print로 출력    
print('My favorite season is ' + season + '.' +       #+를 사용했기 때문에 띄어쓰기를 맞춰서 씀
      ' I was born on the ' + str(int(date)) +'th.')  #str(int(date))을 보면 date가 float라서 소수점(.0)이 나오므로
                                                      #int로 바꿔 소수점을 없애줌
                                                      #그런데 +는 str만 연결할 수 있기 때문에 date형식을 다시 str로 바꿔서 연결함



