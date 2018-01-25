# 클래스
# 변수와 그것과 관련된 함수 하나의 이름으로 정의한것
# 클래스는 메서드, 속성, 클래스변수, 인스턴스 변수로 구성
# 덧붙여 생성자
"""
클래스 정의
 class 이름:
    생성자
    함수정의(메서드)
"""
# 파이썬에는 생성자나 메서드 정의시 암시적으로 첫번째 매개변수가 self로 지정되어 있음
# self는 항상 객체 자기자신을 가리키는 의미로 사용.

# 클래스 이 멤버변수는 생성자를 통해서 정의
# 파이썬에서는 객체로 생성된 후에도 멤버변수를 추가할수있음

class HelloPython:
    def sayHello(self):
        print('Hello~Python!!')


print(HelloPython)
print(type(HelloPython))

#HelloPython.sayHello()
py = HelloPython() #객체를 생성하는게 가장 무난!
py.sayHello()



class Animal:
    type ='동물' # 클래스 수준 변수

    def __init__(self,name,age): # self 는 java의 this와 비슷! 객체 자신을 가리키는 의미!
        self.name=name
        self.age=age

    def eat(self):
        print("먹는다")

# 객체선언 및 사용 : 객체명.메서드
#tiger=Animal()
tiger = Animal('',0)
print(tiger.eat()) #메서드 호출
print(tiger.type) # 인스턴스 변수
print(Animal.type)# 클래스 변수

#생성자를 통해 정의된 인스턴스 변수들
tiger.name='호랑이'
tiger.age=14
tiger.gender='남'
print(tiger.name)
print(tiger.age)
print(tiger.gender)

zibra=Animal('얼룩말',35)
#print(zibra.gender) #존재하지 않는 멤버변수 호출

# 클래스 상속


"""
class 클래스명(부모클래스명)
        클래스 정의
"""


class Tiger(Animal):
    def eat(self):
        print("호랑이는 고기를 먹는다.")

class zibra(Animal):
    def eat(self):
        print("풀뜯어먹는소리하네")


t1=Tiger('혜교',12)
t1.name
t1.eat()
z1=zibra('지현',12)
z1.name
z1.eat()

Animals=[z1,t1] # 객체 지향의 다형성을 이용해서
for ani in animals:
    ani.eat