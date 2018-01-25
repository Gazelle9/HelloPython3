
#이름짓기
# 파스칼 표기법 :첫단어를 대문자로 시작하며 이름을 지음
    # 예 ) Employees, Departments
    # 예 ) RegisterEmployee, JoinMember -> 주로 클래스 만들때
# 카멜 표기법 : 첫단어를 소문자로 시작하여 이름을 지음
    # 예) registerEmployee, joinMember
# 스네이크 표기법 : 소문자와  '_' 기호를 이용해서 이름을 지음
    # 예 ) register_employee, join_member -> 함수나 변수에
# 헝가리언 표기법 : 자료형을 의미하는 접두사를 이용해서 이름을 지음
    # 예 ) strName, isMarried, boolMarried

import random

#def compareRoom():
  #  if CRoomA > CRoomB:
  #      print('방A가 낫다!')
#    elif CRoomA < CRoomB:
 #       print('방 B가 낫다!')
 #   else:
#        print('동일한 가격!')
 #   return (width * height) / Price1





cc = 3000000000  # constant capital 불변자본
vc = 1500000000  # variable capital 가변자본
sv = 4500000000  # surplus value 잉여가치(순수익)


def computeProfit():
    cc = int(input('불변자본을 입력하세요 >'))
    vc = int(input('가변자본을 입력하세요 >'))
    sv = int(input('잉여가치를 입력하세요 >'))
    values= sv / (cc + vc)
    return values

print (computeProfit())

def getExchangeRate(country):
    rate=0
    if country =='us':
        rate=1071
    elif country == 'euro':
        rate=1309
    return rate


byUSD = 780*getExchangeRate('us')
byEUR = 780*getExchangeRate('euro')

if byUSD > byEUR:
    print('유로화로 구입하는게 더 싸네요')
else:
    print('달러로 구입하는게 더 싸네요')


#12

def howMaryRun(radius):
    pi=3.14
    return radius*pi

studentA=howMaryRun(100)
studentB=howMaryRun(90)

print ('학생A는 학생B보다 %d m 더 달렸다.' %(studentA-studentB))


#17 계산기
def intCalu():
    num1=int(input('좌변값을 하나 입력하세요'))
    num2=int(input('우변값을 하나 입력하세요'))
    fmt= "%d + %d = %d \n%d - %d = %d \n"
    fmt +="%d * %d = %d \n%d / %d = %.3f \n"
    fmt +="%d ** %d = %d"

    print (fmt %(num1, num2,num1+num2,\
                 num1, num2, num1-num2,\
                 num1, num2, num1*num2,\
                 num1, num2, num1/num2,\
                 num1, num2, num1 ** num2))
intCalu()


def computeTex():
    mary = input("결혼여부를 입력하세요 (Y/N)").upper()
    if mary == 'Y':
        salary = int(input("연봉을 입력하시오(숫자만입력) > "))
        if salary >= 3000:
            tax= salary * 0.25
        else:
            tax = salary * 0.1
    elif mary == 'N':
        salary = int(input("연봉을 입력하시오(숫자만입력) > "))
        if salary >= 6000:
            tax = salary * 0.25
        else:
            tax = salary * 0.1
    else:
        print("Y 또는 N 만 입력하세요")
    fmt ="연봉 : %d, 결혼여부 : %s, 세금 : %.1f"
    print(salary,mary,tax)
computeTex()

# 윤년여부
def isLeapYear():
    year = int(input("년도를 입력하세요. (19xx or 20xx)"))
    isleap='윤년이 아닙니다'
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        isleap="윤년 입니다."
    print("%d는 %s"%(year,isleap))
isLeapYear()

# 복권 발행
def rouletteLotto():
    luck = input("숫자 세자리를 입력하세요.")
    lotto = str(random.randint(100, 999))
    match = 0 # 일치 여부
    prize= '꽝 다음 기회에!~'
    for i in[0,1,2]:
     for j in [0,1,2]:
            if(luck[i]==lotto[j] or\
               luck[i] == lotto[j] or\
               luck[i] == lotto[j]):
              match +=1
    if match == 3:
        prize="1등 당첨 ㅆㅅㅌㅊ ㄱㅇㄷ인부분!"
    elif match == 2:
        prize = "2등 당첨 ㄱㅇㄷ!"
    elif match == 1:
        prize = "3등 당첨 ㄲㄲ!"
    print (luck,lotto,prize)
rouletteLotto()