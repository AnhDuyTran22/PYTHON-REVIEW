from math import*

class ThiSinh:
    def __init__(self,ma,ten,toan,ly,hoa):
        self.ma = ma
        self.ten = ten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa

    def get_khu_vuc(self):
        return int(self.ma[2])
    
    def infor(self):
        print(self.ma + ' ' + self.ten + ' ' + str(self.get_khu_vuc()),end = ' ')
        tong_diem = self.tong + self.ly + self.hoa
        kv = self.get_khu_vuc()
        if kv == 1:
            tong_diem += 0.5
        elif kv == 2:
            tong_diem += 1
        else:
            tong_diem += 2.5
        if tong_diem == int(tong_diem):
            print(int(tong_diem),end = ' ')
        else:
            print('%.1f' % tong_diem,end = ' ')
        if tong_diem >= 24:
            print('TRUNG TUYEN')
        else:
            print('TRUOT')

if __name__ == '__main__':
    n = ThiSinh(input(),input(),float(input()),float(input()),float(input()))
    n.infor()