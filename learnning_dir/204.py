#定義一個類，有兩個init屬性，a和b,有一個sum方法，求這兩個屬性的和
class Basic:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

i = Basic(2,3)

print(i.a,i.b,i.sum())
