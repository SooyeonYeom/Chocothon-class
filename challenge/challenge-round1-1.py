# Challenge 1

# 문제 1) 변수를 선언하여 이름을 넣고 출력해보세요.

# 문제 2) 사용자로부터 숫자 2개를 입력받고, 두 숫자의 곱을 출력하는 함수를 만드세요.


name = input("당신의 이름은 무엇인가요?")

print(f"{name}..예쁜 이름이네요!")

num = int(input("당신이 가장 좋아하는 숫자는 무엇인가요?"))

num2 = int(input("당신이 두번째로 좋아하는 숫자는 무엇인가요?"))

result = num * num2

print(f"흠.. {name}님이 좋아하는 두 숫자를 곱하면 {result}가 나오네요.")
