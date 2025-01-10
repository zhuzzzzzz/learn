class UppercaseMeta(type):
    def __new__(cls, name, bases, dct):
        # 将所有属性名转换为大写
        uppercase_attributes = {
            key.upper(): value for key, value in dct.items()
        }
        # 使用创建的大写属性字典来创建类
        return super().__new__(cls, name, bases, uppercase_attributes)


class MyClass(metaclass=UppercaseMeta):
    my_attr = "hello"
    another_attr = "world"


# 测试是否存在大写的属性
print(hasattr(MyClass, 'my_attr'))  # False，因为原属性名已经变成大写
print(hasattr(MyClass, 'MY_ATTR'))  # True，因为属性名变成了大写
print(hasattr(MyClass, 'another_attr'))  # False
print(hasattr(MyClass, 'ANOTHER_ATTR'))  # True
