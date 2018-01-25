#파이썬 자료구종
#리스트 squence 자료구조를 사용
#sequence : 순서가 있는 데이터 구조를 의미
# 리스트 , 튜블, 레인지, 문자열등이 sequence구조 사용
#리스트는 []을 사용하여 각 요소에 접근할수있다
from builtins import print

msg='Hello, World!'


#파이썬에서는 자료구조를 의미하는 접미사를 변수명에 사용하기도 한다.
list1_list=[] #빈 리스트
list2_list=[1,2,3,4,5,6,7,8] #숫자
list3_list=['a','b','c','d','e','f','g','h'] #문자
list4_list=['a','b','c','d',1,2,3,True] #혼합

# 간단한 연산
#요소존재여부 파악 : in/not in연산자
print(1 in list1_list)
print('a' in list1_list)
print(3 in list2_list)
#연결 연산
print(list1_list+list3_list)
#반복 연사 :*
print(list2_list*2)\
# 요소의 특정ㅋ값 참조 :index 사용
list2_list[2]=-3
print(list2_list)



#리스트 관련 통계함수
print(sum(list2_list))
#리스트가 주어지면 이것의 가운데에 있는 요소값을 출력

#[1,2,6,8,4]
aa=[1,2,6,8,4]
bb=[1,2,3,4,5,6]
size=len(aa)
mid=int(size/2)
print('가운데값: ',aa[mid]) # 요소 수가 홀수
print('가운데값:',bb[mid-1:mid+1]) # 요소 수가 짝수


def listcenter(list):
    size =len(list)
    mid = int(size/2)
    if size%2==0: # 요소가 짝수
        print('가운데값:', list[mid - 1:mid + 1])
    else: # 요소가 홀수
        print('가운데값: ', list[mid])

listcenter([1,2,3,4])

listcenter([1,2,3,4,5])


# 리스트 조작함수
# 요소추가 : append
list =[1,2,3,4,5]
list.append(9)
list.append(8)
print(list)
# 요소 추가 :insert(위치, 값)

list.insert(6,7)
print(list)

# 요소제거 : remove (값)
list.remove(9)
print(list)


# 요소제거 :pop() , pop(위치)
list.pop(5)
print(list)
list.pop() # 마지막 요소 제거
print(list)
#모두제거 :clear()
list.clear()
print(list)