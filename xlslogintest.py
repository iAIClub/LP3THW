#-*-coding：utf-8-*-
import xlrd
class MoNi(object):
    def pageIndex(self):
        print("#***********************")
        print("*******  A.注册 *********")
        print("*******  B.登录 *********")
        print("*******  C.退出 *********")
        x = input("请输入任意字符： ")
        if x=='a' or x=='A':
            self.regUserIndex()
        elif x=='b' or x=='B':
            self.Login()
        elif x=='c' or x=='C':
            self.Logout()
        else:
            print("输入有误，请重新输入")

    def regUserIndex(self):
        Username=input("请输入用户名：  ")
        flag=self.CheckUserName(Username)
        if flag==0:
            print("用户名不符合要求，请重新输入！")
            exit()
        elif flag==1:
            print("用户名已存在，请重新输入")
            exit()
        else:
            print("恭喜您，用户名可用")
        zz=input("请输入密码")
        self.CheckPwd(zz)
        zzx=input("请再次输入密码")
        if zz==zzx:
            print("恭喜您注册成功")
        else:
            print("密码不一致")


    def Login(self):
        u = input("请输入用户名：")
        p = input("请输入密码： ")
        f = self.CheckUP(u, p)
        if f == 1:
            print("登录成功！")
        else:
            print("用户名与密码不匹配！")

    def Logout(self):
        pass

    def CheckUserName(self,mm):
        l=len(mm)
        if l>=6 and l<=18:
            a=xlrd.open_workbook("/Users/shixin/Desktop/shujuku.xlsx")
            b=a.sheet_by_name("aaa")  #定位Excel内页名称
            for i in range(1,b.nrows):
                if  b.cell(i,0).value==mm :
                    return 1
                else:
                    return 2
        else:
            return 0


    def CheckPwd(self,nn):
        l = len(nn)
        if l <= 20 and l >= 6:
            print("密码合法")
        else:
            print("密码不合法")

    def CheckUP(self,ru,rp):
        a=xlrd.open_workbook("/Users/shixin/Desktop/shujuku.xlsx")
        b=a.sheet_by_name("aaa")
        for i in range(1,b.nrows):
            if b.cell(i,0).value==ru and b.cell(i,1).value==rp:
                return 1
            else:
                return 0






if __name__=="__main__":
    MoNi().pageIndex()
'''
作者：小崔没有钱
链接：https://www.jianshu.com/p/c919d6d49b9d
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
