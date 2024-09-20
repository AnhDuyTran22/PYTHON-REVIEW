from math import*

class NhanVien:
    def __init__(self,ma,ten,gt,ns,dc,mst,hd):
        self.ma = format(ma,'05d')
        self.ten = ten
        self.gt = gt
        self.ns = ns
        self.dc = dc
        self.mst = mst
        self.hd = hd
    
    def chuan_hoa(self):
         if self.ns[1] == '/':
              self.ns = '0' + self.ns
         if self.ns[4] == '/':
              self.ns = self.ns[0:3] + '0' + self.ns[0:3]
         if self.hd[1] == '/':
              self.hd = '0' + self.hd
         if self.hd[4] == '/':
              self.hd = self.hd[0:3] + '0' + self.hd[3:]


    def __str__(self):
        return f'{self.ma} {self.ten} {self.gt} {self.ns} {self.dc} {self.mst} {self.hd}'
    

if __name__ == '__main__':
        n = int(input())
        for i in range(n):
            nv = NhanVien(i+1,input(),input(),input(),input(),input(),input())
            nv.chuan_hoa()
            print(nv)