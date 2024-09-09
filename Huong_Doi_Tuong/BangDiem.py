from functools import cmp_to_key
class HocSinh:
    def __init__(self,ma,ten,diem) -> None:
        self.ma = format(ma,'02d')
        self.ma = 'HS' + self.ma
        self.ten = ten
        self.diem = diem[::]
    
    def get_dtb(self):
        dbt = sum(self.diem)/10
        return dbt
    def get_ma(self):
        return self.ma
    def __str__(self):
        res = ''
        dtb =  sum(self.diem)/10
        if dtb >= 9:
            res = 'XUAT SAC'
        elif dtb >= 8 :
            res = 'GIOI'
        elif dtb >= 7:
            res = 'KHA'
        else :
            res = 'YES'
        return f'{self.ma} {self.ten} {dtb:1f} {res}'

def comp(a,b):
    tb1 , tb2 = a.get_dtb(),b.get_dtb()
    if tb1 != tb2:
        if tb1 > tb2:
            if tb1 > tb2:
                return -1
            else:
                return 1
    else:
        ma1,ma2 = a.get_ma(),b.get_ma()
        if ma1 < ma2 : return -1
        else: return 1


if __name__ == '__main__':
    n = int(input())
    a  = []
    for i in range(n):
        h = HocSinh(i + 1,input(),list(map(float,input().split())))
        a.append(h)
    a.sort(key = cmp_to_key(comp))
    for x in a:
        print(x)