from math import *
from functools import cmp_to_key

class MatHang:
    def __init__(self, ma, ten, don_vi, mua, ban):
        self.ma = str(ma)

        while len(self.ma) < 4:
            self.ma = '0' + self.ma

        self.ma = 'MH' + self.ma
        self.ten = ten
        self.don_vi = don_vi
        self.mua = mua
        self.ban = ban

    def __str__(self):
        return f'{self.ma} {self.ten} {self.don_vi} {self.mua} {self.ban - self.mua}'
    
    def get_loi_nhuan(self):
        return self.ban - self.mua
    
    def get_ma(self):
        return self.ma

def cmp(a, b):
    ln1, ln2 = a.get_loi_nhuan(), b.get_loi_nhuan()
    if ln1 != ln2:
        return ln2 - ln1
    else:
        if a.get_ma() < b.get_ma():
            return -1
        else:
            return 1

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        m = MatHang(i+1, input(), input(), int(input()), int(input()))
        a.append(m)

    a.sort(key=cmp_to_key(cmp))
    for x in a:
        print(x)
