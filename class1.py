class cls1:
    val = 0
    def __init__(self , x ):
        self.val = x
        print('I am constructor.')

    def increment(self):
        self.val += 1

    def output(self):
        print('Val = ',self.val)

    def __del__(self):
        print('I am destructor.')

ob1 = cls1(0)
ob2 = cls1(5)

ob1.increment()

ob1.output()
ob2.output()
