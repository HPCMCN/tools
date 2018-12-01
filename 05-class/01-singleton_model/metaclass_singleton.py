# coding = utf-8


class SingletonMetaClass(type):

    @staticmethod
    def __new__(mcs, name, bases, attrs):
        attrs["_instance"] = None
        return super().__new__(mcs, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Singleton(metaclass=SingletonMetaClass):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.__has_init = True


class User(Singleton):
    pass


user1 = User(a=5, b=20)
print(user1.a)
print(user1.b)
user1.a = 10
print(user1.a)
print(user1.b)
user2 = User()
print(user2.a)
print(user2.b)
user2.a = 20
user2.c = 30
print(user2.c)
print(user2.a)
print(user2.b)
