from urllib.request import urlopen
from bs4 import BeautifulSoup

# 파일을 임포트 함

html = urlopen("https://ko.wikipedia.org/wiki/%EB%B6%84%EB%A5%98:%EC%97%B0%EB%8F%84%EB%B3%84_%EA%B3%A0%EB%A0%A4")
# 링크 지정
bsObject = BeautifulSoup(html, "html.parser")
# bsObjact라는 변수에 저 링크를 넣어줌
readf = open("list.txt", 'r')
# list.txt는 중복이 걸러지지 않은 리스트를 담고 있다
# 읽기 모드로 파일을 염(파일이 있으면 초반 수집 과정을 스킵)
loop_max = (len(readf.readlines()))
# 파일의 줄을 읽음
print(loop_max)
# reallist.txt는 중복을 거른 리스트를 담고있다
# 쓰기 모드로 파일을 염
print(loop_max)
readf.close()
# 필요없으니 이제 닫아줌

f2 = open('1List.txt', 'w')
print(loop_max)
if loop_max == 0:
    # 없으면 새로 크롤링 해서 만듬
    print("파일이 없습니다.\n새로 생성합니다")
    f = open('list.txt', 'w')
    for link in bsObject.findAll('div', {'class': 'CategoryTreeSection'}):
        # bsObjact 에서 div 안에있는 class가 CategoryTreeSection인걸 모두 찾는다
        first_links = link.findAll('span')
        # link에서 span 태그를 찾는다
        if first_links[1].text != '(비어 있음)':
            # 비어있는것은 걸러야 하니 !=(~가 아닌)기호를 써서 걸러준다
            url = 'https://ko.wikipedia.org' + link.find('a').attrs['href']
            # 링크가 a태그 안에 자식인 href 태그에 있으니 href의 내용을 가지고 오고 링크가 /wiki로 시작되니 https://ko.wikipedia.org를 붙여줘
            # 서 링크로 바꾼다(첫번째 거르기 완료)
            # 첫번째 거르기에선 비어있는 문서를 전부 지우고 하위 항목이 있는 링크만 수집하였다
            # 2번째 거르기 시작
            print("열심히 수집중입니다")
            html = urlopen(url)
            bsObject = BeautifulSoup(html, "html.parser")
            ke = bsObject.findAll('div', {'class': 'mw-content-ltr'}, {'lang': 'ko'})
            # div태그 안에있는 한글 문서를 모조리 가져온다
            url = ('https://ko.wikipedia.org' + ke[1].find('a').attrs['href'])
            # 그것의 링크를 수집한다(전 주석 참조)
            # 2번째 거르기에선 분류 되있는 문서들의 하위항목에 들어간것이 1차라면 그것을 다시 들어가서 그 년도의 사건의 링크를 수집한다

            html = urlopen(url)
            bsObject = BeautifulSoup(html, "html.parser")
            for tag in bsObject.findAll('a'):
                # 마지막 거르기
                if 'href' in tag.attrs:
                    # tag.attrs에 href 태그가 있다면 링크가 있다는 것이기 때문에 들어가준다
                    if not tag.attrs['href'].startswith('#'):
                        # #으로 시작하는것은 문서가 아니니 문서 안에있는 이상한 링크를 1차로 지워준다
                        if not tag.attrs['href'].startswith('https://ko.wikipedia.org/http://') and tag.attrs[
                            'href'].startswith("/wiki") and tag.attrs['href'].startwith("https://ko.wikipedia.org/wiki/"):
                            # https://ko.wikipedia.org/http:/,/wiki으로 시작하는것은 문서가 아니니 문서 안에있는 이상한 링크를 2차로 지워준다
                            # 걸러진 문서를 저장한다(인물의 사이트가 아닌 2차로 거른것에서 한번 더 들어가 사건으로 가서 그것의 링크를 수집한다)
                            ke = ('https://ko.wikipedia.org' + tag.attrs['href'])
                            # 앞에서도 말했지만 링크는 href 태그 안에 있고 나온것은 /wiki같은 식으로 나와서 도메인을 붙여준다
                            print(ke, file=f)
                            # 파일로 저장한다

if loop_max == 0:
    f1 = open('realList.txt', 'w')
    # 저장한뒤 닫음
    f = open('list.txt', 'r')
    # 리스트를 정리하기 위해 연다
    f2 = open('1List.txt', 'w')
    # 이름이 저장될 리스트 파일을 만들어 둔다
    # 파일 정리 과정
    prev = None
    for line in sorted(open('list.txt')):
        # 파일을 열고 나열한다
        line = line.strip()
        # line 변수를 .strip 함수로 정렬한다
        if prev is not None and not line.startswith(prev):
            # 라인은 한줄이 되었고 중복된것을 제거한다
            f1.write(prev + '\n')
        # 중복된것을 저장한다
        prev = line
    if prev is not None:
        # 똑같은게 없으면
        f1.write(prev + '\n')
        # 바로 저장한다
myFile = open('realList.txt', 'r')
# 파일을 읽어 줄수를 확인하고 그 줄수만큼 반복시킴
loop_max = (len(myFile.readlines()))
print(loop_max)
a = 0
for a in range(a, loop_max):
    with open('realList.txt', 'r') as data:
        lines = data.readlines()
        # 정리된것을 읽어서 배열로 저장한다
        html = urlopen(lines[a])
        # 배열을 1개씩 읽는다
        print(a)
        print(lines[a])
        bsObject = BeautifulSoup(html, "html.parser")
        # 링크를 연다
        if bsObject.findAll('span', {'class': 'mw-headline'}, string='생애') or bsObject.findAll(string='출생'):
            # 사람인지 아닌지 거른다
            # 문서의 이름이 저장되있는 방식이 총 3개여서 3개를 써줫다
            if len(bsObject.findAll('b')[0].findAll('a')) == 0:
                # 첫번째 유형 b태그 안에 자식으로 a태그가 있는것
                ke = bsObject.findAll('b')[0].text
                # 근데 b태그 안에 a태그가 있는 문서는 다른 b태그 안에 a태그가 있는것들이 있다
                # 첫번째 배열은 무조건 이름이라 첫번째껄 가져온다

                # 그것을 정리해준다(태그를 다 땜)
                print(ke)
                f2.write(ke + '\n')
                # 파일로 저장
                a = a + 1

            # 없는것들도 있고 저번 코드에 오류가 생겨서 더 걸러줌
            # 2번째 유형 h1 태그에 바로 있는 유형
            elif len(bsObject.findAll('span', {'class', 'mbox-text-span'})):
                ke = bsObject.findAll('b')[1].text
                # 근데 b태그 안에 a태그가 있는 문서는 다른 b태그 안에 a태그가 있는것들이 있다
                # 첫번째 배열은 무조건 이름이라 첫번째껄 가져온다

                # 그것을 정리해준다(태그를 다 땜)
                print(ke)
                f2.write(ke + '\n')
                # 파일로 저장
                a = a + 1
            elif len(bsObject.findAll('h1')[0].text) == 0:
                ke = bsObject.findAll('h1')[0].text
                # 바로 h1태그를 찾아서 택스트 추출후 1번째 배열을 가져온다(이 유형도 h1태그가 바로 첫번째임)
                print(ke)
                f2.write(ke + '\n')
                # 파일로 저장
                a = a + 1
            # 3번째 유형 h1 태그가 아닌 span태그에 있는 유형
            elif len(bsObject.findAll('span')):
                ke = bsObject.findAll('span')
                # 바로다가 span 찾아서 추출 후 1번째 배열을 가져온다(이 유형은 span태그가 바로 처음)
                print(ke[0].text)
                f2.write(ke[0] + '\n')
                # 저장~
                a = a + 1
# 열려있는 파일 닫아주기(추후 실행시 오류 발생할 가능성도 있어서)
f.close()
f1.close()
f2.close()
