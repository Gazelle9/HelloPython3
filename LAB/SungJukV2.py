# 총점, 평균, 학점
name='name'
kor=90
mat=70
eng=90


def getTotal():
#pass - 함수 작성전 쓰는 더미코드!
    total = kor+mat+eng
    return total


def getAverge():
    total=getTotal()
    average=total/3
    return average



def getGrade():
    average=getAverge()
    grd='가'
    if average > 100 or average >= 90:
        grd='수'
    elif average >= 80:
        grd='우'
    elif average >= 70:
        grd = '미'
    elif average >= 60:
        grd = '양'
    return grd




fmt = '%s %d %d %d %d %.2f %s'
print(fmt % (name, kor, eng, mat, getTotal(), getAverge(), getGrade()))
