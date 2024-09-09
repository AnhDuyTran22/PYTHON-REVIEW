from sys import stdin

class SinhVien:
    def __init__(self,ma,ten,lop,email):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.email = email

    def chuan_hoa(self):
        tmp = self.ten.split()
        self.ten = ' '.join(tmp).title()
    def get_ma(self):
        return self.ma
    def get_lop(self):
        return self.lop
    def get_khoa(self):
        return self.ma[0:4]
    def __str__(self) -> str:
        return f'{self.ma} {self.ten} {self.email} {self.lop}'

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        s = SinhVien(input(),input(),input())
        s.chuan_hoa()
        a.append(s)
    q = int(input())
    for _ in range(q):
        khoa = input()
        print('DANH SACH SINH VIEN LOP',khoa,':')
        for x in a:
            if x.get_khoa() == khoa:
                print(x)