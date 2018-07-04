try:
    i = int(input('임의의 양의 정수를 입력하세요: '))
    if type(i) == int and i>1:
            for j in range(2,i):
              if i % j == 0 :
                    print('{} x {} = {}\n이 숫자는 소수가 아닙니다.'.format(j, int(i/j), i))
                    break
            else:
                print('이 숫자는 소수입니다.')
    else:
        raise ValueError
except ValueError:
    print('ValueError: 1보다 큰 양의 정수를 입력하세요.')


    
<교수님 답>
while True:
    try:
       i = int(input('임의의 양의 정수를 입력하세요. '))
       if not isinstance(i, int) or i <2 :
            raise ValueError
    except ValueError :
        print('ValueError: 1보다 큰 양의 정수를 입력하세요.')
        continue
    else:
        break



# ----- 소수확인
for n in range(2, i-1):
    if i % n == 0:
        print('{} x {} = {}'.format(n, i//n, i))
        print('이 숫자는 소수가 아닙니다.')
        break
else:
    print('이 숫자는 소수입니다.')
    
