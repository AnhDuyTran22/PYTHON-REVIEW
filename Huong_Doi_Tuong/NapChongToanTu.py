class SoPhuc:
    def __init__(self,thuc,ao):
        self.thuc = thuc
        self.ao = ao
    
    def __add__(self,other):
        self.thuc += other.thuc
        self.ao += other.ao


    def __str__(self):
        return f'{self.thuc} + {self.ao}j'
    
if __name__ == '__main__':
    s1 = SoPhuc(3,2)
    s2 = SoPhuc(3,1)
    s3 = s1 + s2
    print(s1)
    print(s3)