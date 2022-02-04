# 비교연산자

print(1 < 2)
print(2 > 3)

print(1 <= 1)
print(3 >= 2)

print(1 == 2)
print(1 != 2)

# 논리연산자

print(True or False)  # 둘 중 하나만 True여도 ㅇㅋ
print(True and False)  # 둘다 Treu여야 ㅇㅋ
print(not False)  # 반전으로 뱉기

print("H" in "Hello")  # a'가 a에 있니?
print("Q" in "Hello")
print("Q" not in "Hello")  # b'는 a에 없지?


## < 조건문 : If >


# 일치 확인

protein = input("오늘은 운동가실 건가요?\n1. 예 \n2. 아니오")

if protein == "1":
    print("좋아요 ㅎㅎ~")

elif protein == "2":
    print("안돼요~^^ 운동가셔야죠~?")

else:
    print("제대로 대답하세요!^^")


ans = int(input("저 몇살 같아 보여요?^_^"))

if 1 <= ans <= 9:
    print("내가 애기에용?")

elif 10 <= ans <= 19:
    print("지금 저보고 미자라는 거에요?")

elif 20 <= ans <= 21:
    print("오~ ㅎㅎ 기분좋네요!")

elif ans == 22:
    print("정확하네용~^^ 정답!")

elif 23 <= ans:
    print("반려입니다 다시 제출하세요~^^")

else:
    print("질문에 대답하세용~^^")


# 불일치 확인

answer = 20

ans2 = int(input("그럼 몇학번이게요~^^?"))

if ans2 != answer:
    print("미쳤어용?")

else:
    print("좀 치네^^?")


# 크기 비교

money = int(input("돈 얼마 있으세용?"))

if money >= 7000:
    print = int(money)

elif 5000 <= money <= 7000:
    print("흠..좀 애매뽕짝데스네")

else:
    print("걸어가자 ㅎㅎ..")


# 불(Boolean) 참/거짓 확인

student = input("학생이신가요?\n[1] 네\n[2] 아니오\n")

if student == "1":
    is_student = True
else:
    is_student = False

if is_student == True:
    print("학생이시군요!")
else:
    print("학생이 아니시군요.")

# pass

card = True

if card:
    pass  # ㅇㅋ 처리 넘겨버려~ 아무것도 실행 안시킴!
else:
    print("헉 카드 두고 왔어!")


# ___________________


## < 반복문 : While >

while True:
    print("반복문")

#'조건'이 True, 즉 있는 한 / 아래를 반복해라

i = 0

while i < 10:
    print(f"i={i} / 아직 10 안됐음!")
    i += 1  # 기존의 i에 뒤에 오는 숫자를 넣어 연산해라

# 즉, 위 while 문의 i는 점점 1씩 늘게 되고,
# 최대 i=9까지 해당 반복문에 돌려지고 10이 되면 반복문 조건에 걸리지 않음!


while dabjeongneo != 1:
    dabjeongneo = input("1번이랑 2번 중에 뭐가 좋아?")
    if dabjeongneo == "1":
        print("흐흠~ 그럴 줄 알았어!")
    else:
        pass


while True:
    dabjeongneo = input("1번이랑 2번 중에 뭐가 좋아?:")
    if dabjeongneo == "1":
        print("흐흠! 그럴 줄 알았어~")
        break
    else:
        pass


while True:
    dabjeongneo = input("1번이랑 2번 중에 뭐가 좋아?:")
    if dabjeongneo != "1":
        continue  # 자신을 감싸고 있는 가장 가까운 반복문의 처음으로 돌아간다
    else:
        print("흐흠! 그럴 줄 알았어~")
        break


# ___________________


## < 반복문 : For >

# 기본
for i in range(1, 11):
    print(i)

# 리스트 출력
family = ["엄마", "아빠", "나", "동생"]

for member in family:
    print(member)

# 리스트 요소 평균값 구하기
heights = [150, 160, 170, 180]
total = 0

for height in heights:
    total += height

print(f"평균 : {total/len(height)}cm")  # len(a)= a안의 갯수를 불러옴! 문자열이라면 문자 수가 나온다


# # ___________________


## < Def & return >


def age(birth):
    age = 2022 - birth + 1
    return age


birth = int(input("몇년도에 응애?"))
print(f"내 나이는 {age(birth)}살이야!")

# if = pass로 탈출
# for,while = break로 탈출
# def = return으로 탈출


# # ___________________


## < 응용 예제 >

from pydoc import text
import keyboard

white = " "
position = " ■"
print(position)
while True:
    if keyboard.read_key() == "d":
        white += " "
        print(white + position)
    elif keyboard.read_key() == "a":
        white = white.replace(" ", "", 1)
        print(white + position)


## < 응용 예제 >

import sys
import time

text = "안녕하세요..."


def typing(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


# 함수는 바보라서 밖에 있는 상황을 모른다.
# 그래서 밖의 어떤 변수가 있는지 전혀 모른채 영향을 받지 않는다.
# 그래서 밖으로 뱉어줄때도 return을 사용해서 뱉으라고 시켜야한다!


typing("저는 포뇨에요")
print(text)
