import random

#윤년여부
def isLeapYear():
    year = int(input("년도를 입력하세요. (19xx or 20xx)"))
    isleap='윤년이 아닙니다'
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        isleap="윤년 입니다."
    print("%d는 %s"%(year,isleap))


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


#계산기(제곱연산추가)
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

