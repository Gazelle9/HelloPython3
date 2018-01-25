# 함수
#''' 함수는 재사용 가능한 프로그램 조각!'''
def sayHello():
    print('hello,world!!')

sayHello()


def sayHello(msg):
    print('hello, ',msg)
    sayHello('자바')
    sayHello('파이썬')
    sayHello('코볼')


def myfunc(param):
    param='함수안에서 생성'
#함수내 지역변수는 함수 안에서만 사용가능
    #함수 밖에서 선언된 변수는 전역변수
    #따라서 지역변수와 이름만 다르다면 어느함수에건 사용가능!!
    print(param)

param='함수밖에서 생성'
print(param)
myfunc(param)

del param

def myfunc2():
    global param #함수 내에서 전역변수 호출
    param='함수에서 전역변수 수정'
    print(param)

param = '함수 밖에서 생성'
print(param)
myfunc(param)

myfunc2()

#함수내에서 전역변수 사용하기
# 함수가 실행한 결과값을 외부에 전달해야할 필요가 있을때

def count(times):
    times +=1
    print(times)

total=0
count(total)

# 수정!
def count():
    global times
    times +=1
    print(times)

times=0
count()
