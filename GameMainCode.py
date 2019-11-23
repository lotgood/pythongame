import time
myFile = open('1List.txt', 'r')
loop_max = (len(myFile.readlines()))
print(loop_max)
if loop_max == 0:
    print("ERROR:파일이 없습니다.\nCrollingMainCode.py를 먼저 실행하신뒤 실행해주세요")
else:
    print("역사 인물 맞추는 게임")
    time.sleep(1)
    print("안녕하세요.")
    time.sleep(1)
    print("저는 역사 고수 자비스입니다.")
    time.sleep(1)
    print("이제부터 역사의 인물을 맞춰봅시다.")
    time.sleep(1)
    print("맞추실 시대를 입력해 주세요.(시대가 부족하나 추가할 예정입니다)")
    time.sleep(1)
    a = int(input("고려시대는 1번 조선시대는 2번 대한제국은 3번 일제 강점기는 4번을 입력해 주세요:"))
    if a == 1:
        print("고려를 선택하셨네요.")
        time.sleep(1)
        print("고려에 대한 간단한 설명이 있겠습니다.")
        time.sleep(1)
        print("고려는 918년 궁예를 축출하고 왕건이 즉위한 이후.\n1392년 이성계에 의해 멸망하기까지 한반도 대부분을 지배하였던 국가입니다.")
        f = open("1List.txt", 'r')
        print(f)
    elif a == 2:
        print("조선 시대를 선택하셨네요.")
        print("조선에 대한 간단한 설명이 있겠습니다.")
        time.sleep(1)
        print("조선은 유학을 통치 이념으로 삼아 한반도를 518년 간 다스렸던 왕조입니다.\n고려 말 신진 사대부의 지지를 등에 업어 무관 이성계가 건국하였고, 고종이 선포한 대한제국으로 계승되었습니다.")
        f = open("2List.txt", 'r')
    elif a == 3:
        print("대한제국을 선택하셨네요.")
        time.sleep(1)
        print("대한제국에 대한 간단한 설명이 있겠습니다.")
        time.sleep(1)
        print(
            "대한제국은 1897년 10월 12일 부터 1910년 8월 29일까지 한반도와 그 부속 도서를 통치하였던 입헌군주제 국가입니다.\n광무개혁 등 근대화를 추진했으나 실패했고 일본제국에 의하여 "
            "멸망하였습니다.")
        f = open("3List.txt", 'r')
    elif a == 4:
        print("일제 강점기를 선택하셨네요.")
        time.sleep(1)
        print("일제 강점기에 대한 간단한 설명이 있겠습니다.")
        time.sleep(1)
        print(
            "일제 강점기는 1910년 8월 29일 ~ 1945년 8월 15일 동안 일본 제국의 식민지로서 일본령 조선이 존재했던 기간을 가리킵니다.\n일제강점기는 한국의 역사에서 한국의 근현대사를 시대별로 "
            "나누었을 때 약 35년 간 이어진 주요 시대 중 하나입니다.")
        f = open("4List.txt", 'r')

    else:
        print("잘못된 입력값입니다.\n프로그램을 재실행해 주시기 바랍니다\n에러코드:0")  # ERRORCODE 0 은 사용자가 잘못된 값을 입력하였을때 생김
