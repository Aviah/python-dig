# The mro algorithm is complex, but as rules of thumb:
# left before right, subclass before superclass


class A:
    foo = 'baz'


class B(A):
    pass


class C(A):
    foo = 'spam'


class D(B, C):
    pass


print(D.__mro__)
print(D.foo)


class C1(B, A):
    pass


class D(A):
    pass


class E(C1, D):
    pass


print(E.__mro__)


class F1:
    pass


class F2(B):
    pass


class G1(F1):
    pass


class G2(F2):
    pass


class M:
    pass


class H1(E, G1, M):
    pass


class H2(E, G2, M):
    pass


print(H1.__mro__)  # B after C1, via E: F1 is not subclass of B
print(H2.__mro__)  # B via F2 *not* via E: F2 is a subclass of B, so it must appear before B
