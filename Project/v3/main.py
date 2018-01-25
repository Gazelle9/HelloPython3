import sys
from . import sjvo, sjsrv
class SungJukV3Main:
   #성적 처리 서비스 객체 생성
    sjsrv=sjsrv.SungJukService()

    def newSungJuk(self):
        str_list=[]
        str_list.append('\n\n\n 추가할 성적데이터를 입력하세요')
        str_list.append('\n 데이터 입력순서는 이름/국어/영어/수학 입니다.')
        str_list.append('\n 예) 이름 00 00 00')
        print(''.join(str_list))

        # 성적데이터를 한줄에서 공백으로 구분해서 입력받음
        n,k,e,m=input('').split()


        # 입력받은 성적데이터로 성적 객체 생성
        sj=sjvo.SungJukVO(n, int(k),int(e),int(m))

        # 성적객체를 추가함
        self.sjsrv.addSungJuk(sj)

        print('\n 성적 데이터가 성공적으로 추가되었습니다.\n')

    def showSungJuk(self):
        str_list=[]
        str_list.append('\n\n<< 전체 데이터 출력 >>\n')
        for sj in self.sjsrv.getSungJuk():
            str_list.append(sj)
            #리스트 형태로 결과가 return된것을 for 문으로 다시 하나씩 순환하며 출력!
        str_list.append('\n\n')


        print(''.join(str_list))

#        self.sjsrv.getSungJuk()

        print('\n\n\n')

    def showOneSungJuk(self):
        no=input('\n 검색할 학생 번호를 입력하세요.\n >>')
        str_list=[]
        str_list.append('<< 상세 성적데이터 >>\n')
        str_list.append(self.sjsrv.getOneSungJuk(int(no)))
        str_list.append('\n\n')

        print (''.join(str_list))


    def updateSungJuk(self):
        no=input('수정할 학생 번호를 입력하세요 >>')
        str_list = []
        str_list.append('\n\n\n 수정할 성적데이터를 입력하세요')
        str_list.append('\n 데이터 입력순서는 이름/국어/영어/수학 입니다.')
        str_list.append('\n 예) 이름 00 00 00')
        print(''.join(str_list))

        n,k,e,m=input('').split()
        sj=sjvo.SungJukVO(n,int(k),int(e), int(m))
        sj.sjno=int(no) # 수정할 번호 설정

        self.sjsrv.modifySungJuk(sj)
        print('\n\n수정완료!!\n\n')
    def deleteSungJuk(self):
        no = input("\n삭제할 성적번호를 입력하세요\n>>")

        self.sjsrv.removeSungJuk(int(no))
        print("\n\n삭제 성공!!\n\n")


    def exitSungJuk(self):
        sys.exit(1)



    #메뉴 표시
    def displayMenu(self):
        str_list=[]
        str_list.append('========성적 처리 프로그램========\n')
        str_list.append('==================================\n')
        str_list.append('1. 새로운 성적데이터를 추가합니다.\n')
        str_list.append('2. 전체 성적데이터를 조회합니다.\n')
        str_list.append('3. 성적데이터를 상세 조회합니다.\n')
        str_list.append('4. 성적데이터를 수정합니다.\n')
        str_list.append('5. 성적데이터를 삭제합니다.\n')
        str_list.append('6. 성적처리 프로그램을 종료합니다.\n')
        str_list.append('==================================\n')
        print(''.join(str_list))
    # 파이썬 자료 구조중 dictionary를 이용해서 메뉴 분기시 실행할 함수를 객체 형태로 저장
    menus = {'1': newSungJuk, '2': showSungJuk, '3': showOneSungJuk, '4': updateSungJuk,
             '5': deleteSungJuk, '6': exitSungJuk}
#메뉴 선택후 처리
    def selectMenu(self):
        menu = input('system : 실행할 작업을 선택하세요 >> ')
        self.menus[menu](self)

        # if menu == 1: newSungJuk()
        # elif menu == 2: showSungJuk()
        # elif menu == 3: showOneSungJuk()
        # elif menu == 4: updateSungJuk()
        # elif menu == 5: deleteSungJuk()
        # elif menu == 6: exitSungJuk()


