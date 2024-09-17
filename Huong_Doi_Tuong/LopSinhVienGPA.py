from math import*

class SinhVien:
    def  __init__(self,ma,ten,lop,ngay_sinh,gpa):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.ngay_sinh = ngay_sinh
        self.gpa = gpa

    def chuan_hoa(self):
        if self.ngay_sinh[1] == '/':
            self.ngay_sinh = '0' + self.ngay_sinh
        if self.ngay_sinh[4] == '/':
            self.ngay_sinh = self.ngay_sinh[0:3] + '0' + self.ngay_sinh[3:]
    def __str__(self):
        return f'{self.ma} {self.ten}, {self.lop} {self.ngay_sinh} {self.gpa:.1f}'


if __name__ == '__main__':
        ten = input()
        lop = input()
        ns = input()
        gpa = float(input())
        s = SinhVien('SV001',ten,lop,ns,gpa) 
        s.chuan_hoa()
        print(s)