from math import*

from functools import cmp_to_key

class SinhVien:
    def __init__(self,ma ,ten,lop,ngay_sinh,gpa) -> None:
        self.ma = format(ma,'03d')
        self.ma = 'SV' + self.ma
        self.ten = ten       
        self.lop = lop
        self.ngay_sinh = ngay_sinh
        self.gpa = gpa

    def chuan_hoa(self):
        if self.ngay_sinh[1] == '/':
            self.ngay_sinh = '0' + self.ngay_sinh
        if self.ngay_sinh[4] == '/':
            self.ngay_sinh = self.ngay_sinh[0:3] + '0' + self.ngay_sinh[3:]
        tmp = self.ten.split()
        self.ten = ' '.join(tmp).title()

    def __str__(self):
        return f'{self.ma} {self.ten} {self.lop} {self.ngay_sinh} {self.gpa:.2f}'
    

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = SinhVien(i+1,input(),input(),input(),float(input()))
        s.chuan_hoa()
        print(s)