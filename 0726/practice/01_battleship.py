import random  # 랜덤 모듈 활용

print("================================")
print("        Battle Ship Game        ")
print("            START !!            ")
print("================================")

# 필요에 따라 추가적으로 함수를 만들어 자유롭게 활용할 수 있습니다.
# 각자의 해역에 배를 위치시키는 함수
def set_ship(index, sea):
    idx = int(input('배를 위치시킬 시작점을 고르세요. : '))
    if idx >=1 and idx<=13:
        (player_sea[idx] and player_sea[idx+1] and player_sea[idx+2])==1
        print('*'*30)
        print(f'플레이어의 해역 : {player_sea}')



player_sea = [0] * 15  # 플레이어의 해역
player_attacked = [False] * 15  # 플레이어의 공격 위치 기록

computer_sea = [0] * 15  # 컴퓨터의 해역
computer_attacked = [False] * 15  # 컴퓨터의 공격 위치 기록

round = 1  # 게임 라운드

# 1. 게임 준비
while True:
    pass
    # 1-1) 플레이어의 배 시작 위치 고르기

    # 1-2) 범위를 벗어난 시작점을 고른 경우


# 1-3) 컴퓨터의 배 시작 위치를 랜덤으로 지정합니다.

# 1-4) 플레이어와 컴퓨터의 해역에 각각 배 위치시키기

# 2. 라운드 진행
while True:
    pass
    # 2-1) 플레이어 공격

    # 2-2) 플레이어의 공격 위치 선택

    # 2-3) 플레이어의 공격이 성공한 경우

    # 2-4) 플레이어의 공격이 실패한 경우

    # 2-5) 컴퓨터의 공격 위치 지정
    # 컴퓨터가 공격하지 않은 위치를 나타내는 리스트

    # 2-6) 컴퓨터의 공격이 성공한 경우

    # 2-7) 컴퓨터의 공격이 실패한 경우
