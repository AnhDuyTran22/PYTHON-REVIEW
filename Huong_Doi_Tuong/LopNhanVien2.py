from math import*

class NhanVien:
    def __init__(self,ma , ten ,gioi_tinh,ngay_sinh,dia_chi,thue,hop_dong):
        self.ten = ten
        self.ma = ma
        self.ngay_sinh = ngay_sinh
        self.dia_chi = dia_chi
        self.thue = thue
        self.hop_dong = hop_dong
        self.gioi_tinh = gioi_tinh



    def chuan_hoa(self):
        if self.ngay_sinh[1] == '/':
            self.ngay_sinh = '0' + self.ngay_sinh
        if self.ngay_sinh[4] == '/':
            self.ngay_sinh = self.ngay_sinh[0:3] + '0' + self.ngay_sinh[3:]
            tmp = self.ten.split()
        if self.hop_dong[1] == '/':
            self.hop_dong = '0' + self.hop_dong
        if self.hop_dong[4] == '/':
            self.hop_dong = self.hop_dong[0:3] + '0' + self.hop_dong[3:]
            res = ' '.join(tmp)
            res = res.title()
            self.ten = res

    def __str__(self) -> str:
        return self.ma + ' ' + self.ten + ' ' + self.gioi_tinh + ' ' + self.ngay_sinh + ' ' + self.dia_chi + ' ' + self.thue + ' ' + self.hop_dong
    


if __name__ == '__main__':
    n = NhanVien('0001',input(),input(),input(),input(),input(),input())
    print(n)