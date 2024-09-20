from math import*
from functools import cmp_to_key
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

    def get_ns(self):
         return self.ns
    def get_ma(self):
         return self.ma
    def __str__(self):
        return f'{self.ma} {self.ten} {self.gt} {self.ns} {self.dc} {self.mst} {self.hd}'



def comp(a,b):
     ns1 = a.get_ns()
     ns2 = b.get_ns()
     a1 = list(map(int,ns1.split('/')))
     a2 = list(map(int,ns2.split('/')))
     for i in range(-1,-4,-1):
          if a1[i] != a2[i]:
               return a1[i] - a2[i]


     ma1,ma2 = a.get_ma(), b.get_ma()
     if ma1 < ma2:
          return -1
     else:
          return 1

if __name__ == '__main__':
        n = int(input())
        a = []
        for i in range(n):
            nv = NhanVien(i+1,input(),input(),input(),input(),input(),input())
            nv.chuan_hoa()
            a.append(nv)
        a.sort(key= cmp_to_key(comp))
        for x in a:
             print(x)
            