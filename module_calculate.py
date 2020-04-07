__all__=['add','number']

list1=[1,2,3,4,5]
number=100

def add(*args):
    s=0
    for i in args:
        s+=i
    return s

class Calculate:
    def __init__(self,num):
        self.num=num

    def show(self):
        print('Calculate中的普通方法',self.num)

    @classmethod
    def show1(cls):  # 注意这里是cls，不是self
        print('Calculate中的类方法')

def test():
    print('模块内定义的test方法------')

if __name__=='__main__':
    test()


