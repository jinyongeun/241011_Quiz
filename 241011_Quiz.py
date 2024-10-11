class membership:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

    def info(self):
        member = membership(name, age, number)
        print(f"가입하신 계정의 이름은 {member.name}이며, 나이는 {member.age}, 그리고 연락처는 {member.number} 입니다.")

name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
number = input("연락처를 입력하세요: ")

member = membership(name, age, number)

member.info()