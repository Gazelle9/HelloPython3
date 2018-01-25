
class SungJukService:

    sjdb=[] # 성적 데이터를 저장하는 리스트
    #[1,2,3,4,5,6,7]
    #[(no,n,k,e,m,t,a,g,r),(no,n,k,e,m,t,a,g,r),(no,n,k,e,m,t,a,g,r)........] 객체타입으로 저장된것은 no~r까지 긁어서 재가공이 필요.
# 성적 처리 = 총점/ 평균/ 학점 계산
    def computeSungJuk(self,sj):
        sj.tot = sj.kor+sj.eng+sj.mat
        sj.avg = sj.tot/3

        grd_list='가가가가가가양미우수수'
        sj.grd = grd_list[int(sj.avg / 10)]

# 성적 데이터 추가
    def addSungJuk(self,sj):
        self.computeSungJuk(sj)
        sj.sjno=len(self.sjdb)+1
        self.sjdb.append(sj) # 리스트에 성적 데이터 추가
        print(sj.to_str()) # 추가된 성적 데이터 확인

 # 성적 목록 출력 (부분정보)
    def getSungJuk(self):
        str_list = []
        for sj in self.sjdb:
            str_list.append(sj.to_str_list())
            return str_list

 # 성적 상세 출력
    def getOneSungJuk(self, no):
        if no>len(self.sjdb) or no <0:
            return '\n잘못된 값이 입력되었습니다'

        result = ''
        for sj in self.sjdb:  # sjdb 에서 성적데이터를 하나씩 순환
            if sj.sjno == no:  # 만일 학생번호와 찾는번호가 일치하면
                result = sj.to_str()
                break

        return result

 # 성적 삭제
    def removeSungJuk(self, no):
        self.sjdb.pop(no - 1)

 # 성적 수정
    def modifySungJuk(self, sj):
        self.computeSungJuk(sj)  # 성적 재계산
        self.sjdb[sj.sjno - 1] = sj  # 성적데이터 수정

        return self.sjdb[sj.sjno - 1].to_str()  # 수정된 데이터 확인

