myFile = open('1List.txt', 'r')
loop_max = (len(myFile.readlines()))
print(loop_max)
k = 0
i = 0
if loop_max == 0:
    print("ERROR:파일이 없습니다.")
else:
    print("역사 인물 맞추는 게임\n안녕하세요.\n저는 역사 고수 자비스입니다.\n이제부터 역사의 인물을 맞춰봅시다.\n맞추실 시대를 입력해 주세요")
    a = int(input("고려시대는 1번 조선시대는 2번 대한제국은 3번 일제 강점기는 4번을 입력해 주세요:"))
    if a == 1:
        print("고려를 선택하셨네요.")
        print("고려에 대한 간단한 설명이 있겠습니다.")
        print("고려는 918년 궁예를 축출하고 왕건이 즉위한 이후.\n1392년 이성계에 의해 멸망하기까지 한반도 대부분을 지배하였던 국가입니다.")
        Lists = []
        file = open("1List.txt", "r")
        for line in file:
            Lists.append(line.strip('\n'))
        print(Lists)
        file.close()
        f = open("1list.txt", 'r')
        loop_max = (len(f.readlines()))
        while True:
            put = input("알고있는 인물을 입력하세요:")
            for k in range(k, loop_max):
                if Lists[k] == put:
                    print("맞추셧습니다!")
            k = 0
            if i == loop_max:
                print("모든 인물을 맞추셨습니다 대단합니다!")
                break
    elif a == 2:
        print("조선 시대를 선택하셨네요.")
        print("조선에 대한 간단한 설명이 있겠습니다.")
        print("조선은 유학을 통치 이념으로 삼아 한반도를 518년 간 다스렸던 왕조입니다.")
        Lists = []
        file = open("2List.txt", "r")
        for line in file:
            Lists.append(line.strip('\n'))
        print(Lists)
        file.close()
        f = open("2list.txt", 'r')
        loop_max = (len(f.readlines()))
        while True:
            put = input("알고있는 인물을 입력하세요:")
            for k in range(k, loop_max):
                if Lists[k] == put:
                    print("맞추셧습니다!")
                    i = i + 1
                    k = k + 1
            k = 0
            if i == loop_max:
                print("모든 인물을 맞추셨습니다 대단합니다!")
                break
    elif a == 3:
        print("대한제국을 선택하셨네요.")
        print("대한제국에 대한 간단한 설명이 있겠습니다.")
        print("대한제국은 1897년 10월 12일부터 1910년 8월 29일까지 한반도와 그 부속 도서를 통치하였던 입헌군주제 국가입니다.")
        Lists = []
        file = open("3List.txt", "r")
        for line in file:
            Lists.append(line.strip('\n'))
        print(Lists)
        file.close()
        f = open("3list.txt", 'r')
        loop_max = (len(f.readlines()))
        while True:
            put = input("알고있는 인물을 입력하세요:")
            for k in range(k, loop_max):
                if Lists[k] == put:
                    print("맞추셧습니다!")
                    i = i + 1
                    k = k + 1
            k = 0
            if i == loop_max:
                print("모든 인물을 맞추셨습니다 대단합니다!")
                break
    elif a == 4:
        print("일제 강점기를 선택하셨네요.")
        print("일제 강점기에 대한 간단한 설명이 있겠습니다.")
        print("일제 강점기는 1910년 8월 29일 ~ 1945년 8월 15일 동안 일본 제국의 식민지로서 일본령 조선이 존재했던 기간을 가리킵니다.")
        Lists = []
        file = open("4List.txt", "r")
        for line in file:
            Lists.append(line.strip('\n'))
        print(Lists)
        file.close()
        f = open("4list.txt", 'r')
        loop_max = (len(f.readlines()))
        while True:
            put = input("알고있는 인물을 입력하세요:")
            for k in range(k, loop_max):
                if Lists[k] == put:
                    print("맞추셧습니다!")
                    i = i + 1
                    k = k + 1
            k = 0
            if i == loop_max:
                print("모든 인물을 맞추셨습니다 대단합니다!")
                break
    else:
        print("잘못된 입력값입니다.\n프로그램을 재실행해 주시기 바랍니다\n에러코드:0") # ERRORCODE 0 은 사용자가 잘못된 값을 입력하였을때 생김