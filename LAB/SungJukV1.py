#입력부
print("--성적 처리 프로그램 Ver 1.0--")
name=input("이름을 입력하세요 > ")
kor=input("국어 성적을 입력하세요 > ")
eng=input("영어 성적을 입력하세요 > ")
mat=input("수학 성적을 입력하세요 > ")
tot=int(kor)+int(eng)+int(mat)
avg=int(tot)/3

# 성적처리.
grd='가'
if avg<=100 and avg >= 90:
    grd='수'
elif avg/10>=80:
    grd='우'
elif avg >= 70:
    grd='미'
elif avg>=6:
    grd='양'

# 성적처리 output
print("<학생정보>")
print("이름 : "+name)
print("<성적 정보>")
print("국어"+kor)
print("영어"+eng)
print("수학"+mat)
print("총점"+str(tot))
print("평균"+str(avg))
print("학점"+grd)

print("-Another output!-")
print('%s %s %s %s %d %.2f %s'\
    % (name, kor, eng, mat, tot, avg, grd))
