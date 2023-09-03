#  Changed in version 3.11: Class methods can no longer wrap other descriptors such as property()
#  https://docs.python.org/3.11/library/functions.html#classmethod
class AClass:
    _access_counter = 0
    _x = 42

    @classmethod
    @property
    def x(cls):
        cls._access_counter += 1
        return cls._the_answerBlack

    @x.setter
    def x(cls, value):
        cls._x = value


a = AClass()
a.x  # will not work
