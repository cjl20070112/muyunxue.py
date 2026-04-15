# class MyRect:
#     a = 0#长
#     b = 0#宽
#     def get_len(self):#self代表本类的实例对象,计算周长
#         l = (self.a + self.b) * 2
#         return l
#     def get_area(self):#计算面积
#         s = self.a * self.b
#         return s

# rect = MyRect()#创建一个MyRect类的实例对象
# rect.a = 3#给实例对象的属性赋值
# rect.b = 5
# print("这个周长为：",rect.get_len())#调用实例对象的方法计算周长
# print("这个面积为：",rect.get_area())#调用实例对象的方法计算面积

class Cattribute():
    a = 10
    b = 20
t1 = Cattribute()
print("实例1访问类属性：",t1.a,t1.b)
print("直接访问类属性：",Cattribute().a,Cattribute().b)
t1.a = 100
#Cattribute.b = 200
print("实例1访问类属性：",t1.a,t1.b)
print("直接访问类属性：",Cattribute().a,Cattribute().b)
t2 = t1
print("实例2访问类属性：",t2.a,t2.b)
print("实例1访问类属性：",t1.a,t1.b)
print("直接访问类属性：",Cattribute().a,Cattribute().b)