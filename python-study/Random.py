# random 모듈 공부
import random  # random 모듈 임포트


list = [1, 2, 3]

random.random()  # 0부터 1 사이의 실수를 랜덤으로 추출해옴
random.uniform(a, b)  # a이상 b 이하의 실수를 랜덤으로 추출해옴
random.randint(a, b)  # a이상 b 이하의 정수를 랜덤으로 추출해옴
random.randrange(start, stop, step)  # a이상 b이하, a에 c만큼 더해가면서 랜덤으로 추출해옴

one_ran = random.choice([list])
# random.choice(a) : a(리스트)에 있는 값 중 하나를 랜덤으로 추출해옴 (*중복안됨)

more_ran = random.sample([list], 2)
# random.sample(a, b) : a(리스트)에 있는 값을 정한 수(b)만큼 랜덤으로 추출해옴 (*중복안됨)

order_ran = random.shuffle([list])
# random.shuffle(a) : a(리스트)에 있는 값의 정렬 순서를 랜덤하게 바꾼다

for_ran = [random.choice(list) for i in range(2)]
# random.choice(a) for i in range(2) : a(리스트)에 있는 값 중 2개를 랜덤으로 추출해옴 (*중복허용)
# 결과로 2개 값이 나와야 하니, 리스트로 추출해야됨


## <그렇다면, 리스트에 있는 값을 여러번 추출하되 중복되지 않게 할려면 어떻게 해야되나?>


list = []
nums = random.randint(1, 10)

for i in range(3):
    while nums in list:
        nums = random.randint(0, 10)
    list.append(nums)

list.sort()
print(list)


# 리스트라는 공간을 만들어준다
# 1과 10사이의 정수를 랜덤으로 추출해주는 함수를 설정한다
# for문으로 리스트에 3개의 숫자가 들어가도록 반복해준다
# while문으로 중복이 되지 않게 만든다. While문은 True일때 실행된다.
# 즉, nums에서 뽑힌 숫자가 list에 존재할 때 -> 한번 더 뽑는다
# 만약 리스트에서 뽑힌 숫자가 list에 존재하지 않을 때 -> while문 탈출, for문으로 돌아간다.
# list.append(nums)로 list의 끝에 랜덤추출된 수 nums를 추가하고, lisr.sort()로 항목을 오름차순으로 정렬해준다.


