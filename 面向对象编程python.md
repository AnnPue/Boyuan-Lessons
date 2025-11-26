# 博远技术分享2

## 面向对象程序设计

OOP：对一个对象需要进行什么操作

1.高复用 2.可维护 3.扩展 4.符合人类思维

### 类Class

属性：类中变量

方法：类中函数

对象：根据类来创建的实例

思想：

封装：1.数据隐藏  2.接口和实现相分离

继承：子类可以继承父类特性，可复用

~~~
class MyCar():
    def __init__(self, brand)
    def drive()
    def wipe()
class EleCar(MyCar):
class FuelCar(MyCar):
~~~

多态：相同接口相同操作对不同对象可以实现不同效果

## 上下文管理

数据持久化：用json文件保存之前数据