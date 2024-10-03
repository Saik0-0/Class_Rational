import math


class Rational:
    def __init__(self, numer, denomin):
        self.numer = numer
        self.denomin = denomin
        self.check()

    def check(self):
        #   0 в знаменателе
        if self.denomin == 0:
            print('Wrong denominator')
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
        if self.denomin == other.denomin:
            self.numer += other.numer
        else:
            self.numer = self.numer * other.denomin + other.numer * self.denomin
            self.denomin *= other.denomin
        return self

    def __sub__(self, other):
        if self.denomin == other.denomin:
            self.numer -= other.numer
        else:
            self.numer = self.numer * other.denomin - other.numer * self.denomin
            self.denomin *= other.denomin
        return self

    def __pow__(self, power, modulo=None):
        self.numer **= power
        self.denomin **= power
        return self

    def __mul__(self, other):
        self.numer *= other.numer
        self.denomin *= other.denomin
        return self

    def __truediv__(self, other):
        self.numer *= other.denomin
        self.denomin *= other.numer
        return self
