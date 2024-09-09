class SinhVien:
    def __init__(self,ma,ten,lop,email) -> None:
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.email = email
    
    def get_ma(self):
        return self.ma
    def get_lop(self):
        return self.lop
    def __str__(self):
        return f'{self.ma} {self.ten} {self.lop} {self.email}'
    


if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        s = SinhVien(input(),input(),input())
        a.append(s)
    a.sort(key=lambda x : (x.get_lop(), x.get_ma()))
    for x in a:
        print(x)