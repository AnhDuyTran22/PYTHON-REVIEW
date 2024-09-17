from math import*

class GiaoVien:
    def __init__(self,ma,ten,luong_co_ban):
        self.ma = ma
        self.ten = ten
        self.luong_co_ban = luong_co_ban

    def get_he_so(self):
        return int(self.ma [2 : ])
    
    def get_thu_nhap(self):
        he_so = self.get_he_so()
        luong = he_so*self.luong_co_ban
        cv = self.ma[0:2]
        if cv == 'HT':
            return luong + 2000000
        elif cv == 'HP':
            return luong + 900000
        else:
            return luong + 500000
    
    def __str__(self):
        return f'{self.ma} {self.ten} {self.get_he_so()} {self.get_thu_nhap()}'
    


if __name__ == '__main__':
    g = GiaoVien(input(),input(),int(input()))
    print(g)