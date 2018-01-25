# 모듈 사용하기
# 프로그램을 구성하는 독립적인 단위를 각각 정의하고 관리하는 방법.
# 자주 사용하는 일반적인 기능은 오듈로 한번 만들어두면
# 필요할때마다 도입해서 활용할수 있다.
# 모듈 : 관련성있는 데이터들, 함수, 클래스

# 모듈을 사용하려면 import명령으로 인터프리터에게 사용여부를 알려야 한다
import random
import math
#import Lab03
#import random as r ->  별칭으로 줄여쓰기
from random import randint #-> 모듈명을 아예 줄여쓰기
from math import pi,sqrt
import sizk as siz
from sizks.Hello import sayHello

sayHello()


# 모듈을 호출할때는 모듈명(파일이름).함수명
#print(random.randint(1,10))
#print(math.pi)
#print(math.sqrt(9))

# 모듈 호출시 이름을 별칭으로 바꿔 정의
# import 모듈이듬 as 별칭
##print(r.randint(0,5))

# 함수 호출시 모듈명
#print(radint(0,5))


# 사용자가 만든 모듈을 다른 파일에서 참조하려면
# 두 파일이 모두 같은 위치에 있어야함
# 즉, 프로젝트 내에서 서로 참조하려면 이 파일들은 같은 위치에 저장되어야한다.







