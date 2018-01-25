#성적처리 프로그램 V3
# 이름 국어 영어 수학 총점 평균 학점

name_list=[]
kor_list=[]
eng_list=[]
mat_list=[]
tot_list=[]
avg_list=[]
grd_list=[]

"""name_list.append(input("이름을 입력하세요 > "))
kor_list.append(int(input("국어 성적을 입력하세요 > ")))
eng_list.append(int(input("영어 성적을 입력하세요 > ")))
mat_list.append(int(input("수학 성적을 입력하세요 > ")))
tot_list.append(kor_list[1] + eng_list[1] + mat_list[1])
avg = int(tot_list[1]) / 3

print(name_list, kor_list, eng_list, mat_list, tot_list, avg_list)
fmt = '%s %d %d %d %d%.2f %s'
print(fmt % (name_list[n], kor_list[n], eng_list[n], mat_list[n], tot_list[n], avg_list[n]))
"""
def getGrd():

    if avg_list[idx] > 100 or avg_list[idx] >= 90:
        grd='수'
    elif avg_list[idx] >= 80:
        grd ='우'
    elif avg_list[idx] >= 70:
        grd = '미'
    elif avg_list[idx] >= 60:
        grd = '양'
    else:
        grd= '가'
    return grd_list.append(grd)

while True:

    idx = len(name_list) # 인덱스 지정
    name_list.append(input("이름을 입력하세요 > "))
    kor_list.append(int(input("국어 성적을 입력하세요 > ")))
    eng_list.append(int(input("영어 성적을 입력하세요 > ")))
    mat_list.append(int(input("수학 성적을 입력하세요 > ")))
    tot_list.append(kor_list[idx] + eng_list[idx] + mat_list[idx])
    avg_list.append(tot_list[idx] / 3)
    # grd_list.append('가')
    getGrd()


    fmt = '%s %d %d %d %d %.2f %s'
    print(fmt % (name_list[idx], kor_list[idx], eng_list[idx], mat_list[idx], tot_list[idx], avg_list[idx], grd_list[idx]))

    is_exit=input('중지하시려면 겠습니까?(Y/N)').upper()
    if is_exit== 'Y':
        continue
    else:
        idx += 1
        print(idx,'명의 학생데이터가 입력되었습니다.')
        break



