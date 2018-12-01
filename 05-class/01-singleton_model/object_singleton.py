# coding = utf-8


class SingletonClass(object):

    @staticmethod
    def __new__(cls, *args, **kwargs):
        if hasattr(cls, "_instance") is False:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, **kwargs):
        if hasattr(self, "_has_init") is False:
            for key, value in kwargs.items():
                setattr(self, key, value)
            self._has_init = True


if __name__ == '__main__':
    class User(SingletonClass):
        pass


    u1 = User(a=5)
    print(u1.a)
    u1.b = 0
    u1.a = 10
    u2 = User()

