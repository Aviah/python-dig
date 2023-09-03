# Not recommended, but possible
class Prop:
    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return obj.foo * 2

    def __set__(self, obj, value):
        obj.foo = value


class Aclass:
    def __init__(self, foo):
        self.foo = foo

    p = Prop()


print(Aclass.p)
a = Aclass(100)
a.m = Prop()
print(a.p)
print(a.m)
