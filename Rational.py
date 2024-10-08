import math
from tkinter.messagebox import showinfo, showerror


class Rational:
    def __init__(self, numer, denomin=1):
        self.numer = numer
        self.denomin = denomin
        self.check()

    def check(self):
        #   0 в знаменателе
        if self.denomin == 0:
            showerror('Error:', 'Wrong denominator')
            self.numer = 0
            self.denomin = 0
            return self

        #   отрицательные числа
        flag_negative = False
        if self.numer < 0 and self.denomin < 0:
            self.numer *= -1
            self.denomin *= -1
        elif self.denomin < 0:
            self.numer *= -1
            self.denomin *= -1
        if self.numer < 0:
            flag_negative = True

        #   ищем общий делитель
        d = math.gcd(self.numer, self.denomin)
        self.numer //= d
        self.denomin //= d

        return self

    def __str__(self):
        return str(self.numer) + '\\' + str(self.denomin)

    def __call__(self):
        print(self)

    def __add__(self, other):
        if isinstance(other, Rational):
            if self.denomin == other.denomin:
                self.numer += other.numer
            else:
                self.numer = self.numer * other.denomin + other.numer * self.denomin
                self.denomin *= other.denomin
        else:
            self.numer += other * self.denomin
        self.check()
        return self

    def __sub__(self, other):
        if isinstance(other, Rational):
            if self.denomin == other.denomin:
                self.numer -= other.numer
            else:
                self.numer = self.numer * other.denomin - other.numer * self.denomin
                self.denomin *= other.denomin
        else:
            self.numer -= other * self.denomin
        self.check()
        return self

    def __pow__(self, power, modulo=None):
        self.numer **= power
        self.denomin **= power
        self.check()
        return self

    def __mul__(self, other):
        if isinstance(other, Rational):
            self.numer *= other.numer
            self.denomin *= other.denomin
        else:
            self.numer *= other
        self.check()
        return self

    def __truediv__(self, other):
        if isinstance(other, Rational):
            self.numer *= other.denomin
            self.denomin *= other.numer
        else:
            self.denomin *= other
        self.check()
        return self
