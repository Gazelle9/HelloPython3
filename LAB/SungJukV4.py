class SungJukV0:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat


class SungJukService: #self는 같은 클래스 내에서 불러들일때
    def getTotal(self, sj):
        tot = sj.kor+sj.eng+sj.mat
        return tot

    def getAverage(self,sj):
        avg=self.getTotal(sj)/3
        return avg

    def getGrade(self,sj):
        grdlist='가가가가가가미양우수수'
        var = int(self.getAverage(sj)/10)
        grd=grdlist[var]
        return grd

sj=SungJukV0('혜교',99,98,11) # 다른 클래스의 값을 각각 집어넣어야하기때문에 sungjukv0의 객체를불러옴

sjsrv = SungJukService()

print(sj.name, sj.kor, sj.eng, sj.mat)
print(sjsrv.getTotal(sj),sjsrv.getAverage(sj),sjsrv.getGrade(sj))