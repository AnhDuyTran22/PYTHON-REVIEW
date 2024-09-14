class Person:
    nationlity = 'Viet Nam'
    def __init__(self,name,job):
        self.name = name
        self.job = job

    def infor(self):
        print(self.name + ' ' + self.job)
    def greet(self):
        print('Xin chao')

if __name__ == '__main__':
    p1 = Person('Teo','Dev')
    p2 = Person('Ty','Engineer')
    p1.infor()
    