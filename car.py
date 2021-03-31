class Car:
    # 속성(클래스/인스턴스 변수)
    num = 0
    color = ''
    speed = 0
    freq = 0

    # 생성자 메서드(Car 객체가 만들어질 때 자동 실행됨)
    def __init__(self, n, c):
        self.num = n
        self.color = c
        self.speed = 0
        print(f"{n} 자동차가 생산되었습니다. ({c})")

    # 기능(메서드)
    def horn(self):
        print(f'{self.num} 자동차가 경적을 울립니다.')
    
    def radio(self, f):
        self.freq = f
        print(f"{self.num} 자동차가 라디오를 켭니다. (주파수: {self.freq})")

    def change_speed(self, v):
        self.speed = self.speed + v
        if self.speed > 200:
            self.speed = 200    # 속력을 200으로 제한
        print(f'{self.num} 차량의 현재 속력: {self.speed}')

# Car 객체 생성(사용)
car1 = Car(1111, 'black')
car2 = Car(2222, 'white')

print(car1.num, car1.color)
print(car2.num, car2.color)

car1.horn()
car2.horn()

car1.change_speed(100)
car1.change_speed(50)
car1.change_speed(-20)

car2.change_speed(50)
car2.change_speed(10)
car2.change_speed(20)

print('-' * 20)

car1.change_speed(100)
car1.change_speed(100)
car1.change_speed(100)

print('-' * 20)

# 라디오 기능을 만들어주세요.(radio)
car1.radio(95.9)
car2.radio(107.7)