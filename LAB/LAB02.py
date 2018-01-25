#18
mary=input("결혼여부를 입력하세요 y/n").upper()

if mary=='Y':
    salary = int(input("연봉을 입력하시오(숫자만입력) > "))
    if salary>=3000:
        print("당신이 납부해야하는 세금은 ", salary * 0.25, "원 입니다.")
    else:
        print("당신이 납부해야하는 세금은 ", salary * 0.1, "원 입니다.")
elif mary=='N' :
    salary = int(input("연봉을 입력하시오(숫자만입력) > "))
    if salary>=6000:
        print("당신이 납부해야하는 세금은 ", salary*0.25,"원 입니다.")
    else:
        print("당신이 납부해야하는 세금은 ", salary * 0.1, "원 입니다.")
else :
    print("Y 또는 N 만 입력하세요")
#19
year=int(input("년도를 입력하세요. (19xx or 20xx)"))
if  (year % 400 ==0) or (year%100!=0) and (year % 4 == 0):
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")

#20
import random
num = input("숫자 세자리를 입력하세요.")
rnum=str(random.randint(100,999))
match=0

if num[0] == rnum[0] or num[0] == rnum[1] or num[0] == rnum[2] :
        match+=1
if num[1] == rnum[0] or num[1] == rnum[1] or num[1] == rnum[2] :
    match += 1
if num[2] == rnum[0] or num[2] == rnum[1] or num[2] == rnum[2]:
    match += 1
print (num, rnum,match)
if match ==3:
    print ("1등")
elif match==2:
    print ("2등")
elif match==1:
    print("3등")
else :
    print ("꽝")

#21
dan = int(input("단수를 입력하세요.(1~9)"))
if dan>=1 and dan<=9:
    for i in range(1,10):
        print('%d X %d = %d' %(dan, i, dan*i))
else:
    print("1~9사이의 문자를 입력하세요")

#21-1
dan2 =input("단수를 입력하세요.(1~9)")
if ord(dan[0]) >= ord('0') and ord(dan[0]) <= ord('9'):
    print('구구단 출력')
    else:
    print('입력오류 -숫자만 입력하세요')
    #22
# 문자 ascii 코드값 ord()
# ascii코드값- 문자 :chr()
char=input("알파벳 소문자를 입력하세요")
if not num.isnumeric() :   #ord(char) >= 97 and ord(char) <= 122 또는 ord(char)>=ord('a') 식으로 써도 가능!
    print(char.upper())
else:
    print("알파벳 소문자만 입력하세요")


#23
# 숫자마추기 게임

# 난수생성 이용
import random
number = random.randint(1, 100)
# 맞출때까지 계속반복
isloop = True
while isloop:
    guess = int(input('숫자를 입력하시오'))
    if guess == number:
        print('정답2-A-YO!!')
        print('근데 상품은 up! sir-YO.!')
        isloop = False  # 실행 종료
    elif guess < number:
        print('응 그거보다 높아여')
    else:
        print('낮아얍!')
print('게임이 끝났써엽!')

#24
print('        Multiplication Table      ')
print('        1   2   3   4   5   6   7   8   9')
print('_________________________________________')

for i in range(1,10):
    print ('%d|      %d   %d   %d   %d   %d   %d   %d   %d   %d'\
             %(i, i*1, i*2, i*3, i*4, i*5, i*6 ,i*7 ,i*8 ,i*9))

#25
cno=input("카드번호를 입력하시오 >")
if cno[0:2]=='35':
    print("jcb카드")
    if cno[5:6] == '17':
        print("NH농협")
    elif cno[5:6]=='01':
        print("신한")
    elif cno[5:6]=='12':
        print("국민")
elif cno[0:2]=='04':
    print("비자")
    if cno[5:6] == '25':
        print("비씨")
    elif cno[5:6]=='53':
        print("신한")
    elif cno[5:6]=='26':
        print("국민")
elif cno[0:2]=='51':
    print("마스터")
    if cno[5:6] == '94':
        print("신한")
    elif cno[5:6]=='53':
        print("신한")
    elif cno[5:6]=='26':
        print("국민")


#26
jm= input("주민등록번호 > ")
logic = [2,3,4,5,6,7,8,9,2,3,4,5]
number = 0
for i in range(0, len(logic)):
    number += int(jm[i]) * int(logic[i])
if 11-(number%11) == int(jm[12]):
    print("이 주민등록번호는 유효한 주민등록번호 입니다.")
else:
    print("이 주민등록번호는 유효하지 않은 주민등록번호 입니다.")


total=0
while True:
    num = input('더할숫자는?(종료:stop)')
    if num =='stop':
        break
    if ord(num[0]) <ord('0') or ord(num)>ord('9'):
        continue #숫자가 아니면 합산 건너뜀

total+=int(num)
print ('합계: ',total)
