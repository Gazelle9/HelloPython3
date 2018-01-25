# print()를 이용 다음 내용을 출력.
print("-------1번-------")
print("▒  ▒  ■■  ■■■  ■■■  ■   ■")
print("▒  ▒ ■  ■ ■  ■ ■  ■ ■   ■")
print("▒  ▒ ■  ■ ■  ■ ■  ■ ■   ■")
print("▩▩▩▩ ▩▩▩▩ ▩■▩  ▩■▩   ▩■▩ ")
print("▒  ▒ ■  ■ ■ ■  ■ ■    ■  ")
print("▒  ▒ ■  ■ ■  ■ ■  ■   ■  ")
print("▒  ▒ ■  ■ ■  ■ ■  ■   ■  ")

print("  ///// ")
print(" | o o |")
print("(|  ^  |)")
print(" | ▷ ◁ |")
print(" |-- --|")
print("                    +---+")
print("                    |   |")
print("                +---+---+")
print("                |   |   |")
print("            +---+---+---+")
print("            |   |   |   |")
print("        +---+---+---+---+")
print("        |   |   |   |   |")
print("    +---+---+---+---+---+")
print("    |   |   |   |   |   |")
print("+---+---+---+---+---+---+")
print("|   |   |   |   |   |   |")
print("+---+---+---+---+---+---+")

print(" /\_/\       _______ ")
print("( I I )     / Hello \ ")
print("(  -  )    <  junior |")
print(" | | |      \ coder!/")
print("(__|__)      ------- ")

#2. 이름 나이 몸무게
print("------2번--------")
name="아이유"
weight=55
age=24
print(name,weight,age)

#3. 수학식을 파이썬 표현식으로 작성
print("-------3번-------")
x=2
y=3
z=4
print('3x = ',3+x)
print('3+x+y = ',3+x + y)
print('x+y/7 = ',x+y/7)
print('(3*x+y)/(z+2) = ',(3*x+y)/(z+2))



#4. 다음 표현식을 완성
print("-------4번-------")
x,y=4,8
x*=y
print('x*=y:',x)

x-=y
print('x-=y:',x)

#5. 다음 수식을 파이썬으로 작성
print("-------5번-------")
x=3
print(x+7==10)

#6. 다음 표현식의 결과는?
print("-------6번-------")
a=(-32+95)*12/3
b=(3*4-((-27+67)/4))**8
c=(512+1968+432)/(2**4)+128
d=256==2**8
e=50+50<=10*10
f= 99 != (10**2)-1
print(a,b,c,d,e,f)
#7 변수에 정의된 값을 이용해서 표현식의 실행결과는?
print("-------7번-------")
x=2.5
y=-1.5
m=18
n=4
print(x+n*y-(x+n)*y)
print(m/n+m%n)
print(5*x-n/5)
print(1-(1-(1-(1-(1-n)))))

#8.
print("-------8번-------")
RoomA=(2.5*3)/27
RoomB=(4*2)/30
print("방A : ",RoomA)
print("방B : ",RoomB)
print(RoomA<RoomB) #A방 보다 B방이 좋다. -> FALSE

#9.
print("-------9번-------")
print(3+4.5*2+27/8)
print(True or False and 3<4 or not (5==7))
print(True or (3<5 and 6>2))
#print(not True >'a') 문자에 비교연산자
#print(7%4+3-2/6*'z') 문자에 산술연산자
#print('D'+1+'M'%2/3) 문자에 산술연산자
print(5.0/3+3/3)
print(53%21<45/18)
print((4<6)or True and False or False and (2>3))
print(7-(3+8*6+3)-(2+5*2))

#10.
print("------10번------")
cc=3000000000 # constant capital 불변자본
vc=1500000000 # variable capital 가변자본
sv=4500000000 # surplus value 잉여가치(순수익)
print("value = ", sv/(cc+vc))

#11
# 달러(780) - 환율 (1,069.90)
# 유로(650) - 환율 (1,307.79)
print("------11번------")

USD=780*1069.90
EUR=650*1307.79
print("USD : ",USD)
print("EUR : ",EUR)
#12
# 둘레 = 2πr
print("------12번------")
r1=100 #지름이 100m
r2=95
c1=r1*3.14 #외각으로 달릴경우
print("외각:",c1) # 지름이 100m 일경우 둘레는 314.0m
c2=r2*3.14
print("안쪽",c2) # 지름이 95m 일경우 둘레는 298.3m
print(c1-c2)
#13
print("------13번------")
print("check out this line")
print("//hello there"+'9'+str(7)) # int 7 을 str(문자형)으로 변환
print('H'+'I'+"is"+str(1)+"more example") # int 1 을 str(문자형)으로 변환
print('H'+str(6.5)+'I'+"is"+str(1)+"more exaxple")#

#14
print("------14번------")
print(True and False and True or True)
print(True or True and True and False)
print((True and False)or (True and not False)or (False and not False))
print((2<3)or(5>2)and not(4==4)or 9!=4)
print(6==9 or 5<6 and 8<4or 4>3)
#15
print("------15번------")
print(27/13+4)
print(27/13+4.0)
print(427%3+18)
print((3<4) and 5/8)
print(23/5+23/5.0)
print(2.0+int(a))
print(2+int(a))
print('a'+'b')
print(int(a)/int(b))
print(int(a) and not int(b))
#print(int(a)/int(b))

#16 증감연산자는 파이썬에서는 지원되지 않는다.(무쓸모)
print("------16번------")
n=3
print(++n)
print("n==",+n)
print(--n)
print("n==",+n)

#17
fn=int(input("첫번째 정수를 입력하세요 > "))
sn=int(input("두번째 정수를 입력하세요 > "))
print('%d + %d= %d'%(fn,sn,fn+sn))
print('%d - %d= %d'%(fn,sn,fn-sn))
print('%d * %d= %d'%(fn,sn,fn*sn))
print('%d / %d= %d'%(fn,sn,fn/sn))



