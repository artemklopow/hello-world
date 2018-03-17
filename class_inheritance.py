"""Look at the picture!"""


class A:
    pass


class B:
    pass


class C:
    pass


class D(B, A):
    pass


class E(C):
    pass


class F(list, D):
    def is_even_len(self):
        print('It is from F:', len(self) % 2 == 0)

    def summ(self):
        print('It`s from F:', sum(self))


class M:
    def p_len(self):
        print('It`s from M:', len(self))


class G(E, F, M):
    def is_even_len(self):
        print('It is from G:', len(self) % 2 == 0)


class K(G):
    def is_even_len(self):
        F.is_even_len(self)
    def pop(self):
        x = super(G, self).pop()
        print('Last value =', x)
        return x


a = A()
b = B()
c = C()
d = D()
e = E()
f = F([1, 2])
g = G([1, 2, 3])
k = K([7, 6, 5, 4])
k.p_len()
k.is_even_len()
k.pop()
