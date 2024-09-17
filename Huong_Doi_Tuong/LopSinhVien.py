from math import*

class SinhVien:
    def __init__(self,ten,ngay_sinh,m1,m2,m3) :
        self.ten = ten
        self.ngay_sinh = ngay_sinh
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def __str__(self) :
        tong_diem = m1 + m2 + m3
        return f'{self.ten} {self.ngay_sinh} {tong_diem:.1f}'
    

if __name__ == '__main':
    ten = input()
    ns = input()
    m1 = float(input())
    m2 = float(input())
    m3 = float(input())
    s = SinhVien(ten,ns,m1,m2,m3)
    print(s)