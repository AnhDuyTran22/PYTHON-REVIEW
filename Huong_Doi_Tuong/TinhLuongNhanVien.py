from math import*

class NhanVien:
    def __init__(self,ma,ten,luong,ngay_cong,chuc_vu):
        self.ma= ma
        self.ten = ten
        self.luong = luong
        self.ngay_cong = ngay_cong
        self.chuc_vu = chuc_vu

    def get_luong_thang(self):
        return self.ngay_cong*self.luong
    
    def get_thuong(self):
        luong = self.get_luong_thang()
        if self.ngay_cong >=25:
            return 0.2*luong
        elif self.ngay_cong >= 22:
            return 0.1*luong
        else:
            return 0
        
    def get_phu_cap(self):
        if self.chuc_vu == 'GD':
            return 250000
        elif self.chuc_vu == 'PGD':
            return 200000
        elif self.chuc_vu == 'TP':
            return 180000
        else:
            return 150000
        
    def get_thu_nhap(self):
        return self.get_luong_thang() + self.get_thuong() + self.get_phu_cap()
    

    def __str__(self):
        return f'{self.ma} {self.ten} {self.get_luong_thang()} {self.get_thuong()} {self.get_phu_cap()} {self.get_thu_nhap()}'
    


if __name__ == '__main__':
        n = NhanVien('NV01', input(),int(input()),input())
        print(n)