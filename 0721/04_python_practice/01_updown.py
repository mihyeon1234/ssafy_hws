import random

is_playing = True
print('================================')
print('        Up and Down Game        ')
print('================================')

answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
counts = 0 
while is_playing:
    print('answer : ',answer)
     # 몇 번만에 정답을 맞혔는지 담는 변수
    user = int(input('1이상 10000이하의 숫자를 입력하세요. :'))
    if answer > user:
        counts += 1
        print('UP!!')
    elif answer <  user:
        counts += 1
        print('DOWN!!')
    elif answer == user:
        counts += 1
        print(f'Correct!!! {counts}회 만에 정답을 맞히셨습니다')
        print('게임을 재시작 하시려면 y, 종료하시려면 n 을 입력하세요. : ')
        re = input()
        if re == 'y':
            answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
            counts = 0 
        else:
            print('잘못된 값을 임력하셨습니다. 게임을 종료합니다.')
            break
        