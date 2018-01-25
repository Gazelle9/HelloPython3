print("구구단 생성기")
dan=int(input("단수를 입력하세요 > "))
for n in range(1,20):
    print('%d x %d = %d' \
              %(dan, n, dan*n))

# for 의 또다른 용법

for i in range(1,100,2):
    print (i)

for i in range(2,101,2):
    print (i)

#특정코드단순반복 _는 변수를 사용하지 않는다는 뜻!
n=10
for _ in range(n):
    print('안녕하세용')

# 범위지정의 또다른 방법:RANGE(1,6)
for i in [1,2,3,4,5]:
    print (i)
