from collections import OrderedDict

class Roman:
    def __init__(self, n):
        if type(n) is not int:
            raise TypeError("Roman objects require an integer input")

        if n >= 2000000:
            raise ValueError("Romans only support values smaller than 2,000,000.\n" +
                             "Value was too large.")

        self.val = n
        self.rom = toR(self.val)

    def __str__(self):
        return self.rom

    def __repr__(self):
        return "Roman(" + str(self.val) + ")"


    def __add__(self, other):
        if type(other) is Roman:
            return Roman(self.val + other.val)

        elif type(other) is int:
            return Roman(self.val + other)

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")

    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, other):
        if type(other) is Roman:
            return Roman(self.val - other.val)

        elif type(other) is int:
            return Roman(self.val - other)

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")

    def __rsub__(self, other):
        v = self.__sub__(other)
        v.val = -v.val
        return v


    def __mul__(self, other):
        if type(other) is Roman:
            return Roman(self.val * other.val)

        elif type(other) is int:
            return Roman(self.val * other)

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")

    def __rmul__(self, other):
        return self.__mul__(other)


    def __truediv__(self, other):
        if type(other) is Roman:
            return (Roman(self.val // other.val), Roman(self.val % other.val))

        elif type(other) is int:
            return (Roman(self.val // other), Roman(self.val % other))

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")

    def __rtruediv__(self, other):
        if type(other) is Roman:
            return (Roman(other.val // self.val), Roman(other.val % self.val))

        elif type(other) is int:
            return (Roman(other // self.val), Roman(other % self.val))

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")


    def __floordiv__(self, other):
        if type(other) is Roman:
            return Roman(self.val // other.val)

        elif type(other) is int:
            return Roman(self.val // other)

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")

    def __rfloordiv__(self, other):
        if type(other) is Roman:
            return Roman(other.val // self.val)

        elif type(other) is int:
            return Roman(other // self.val)

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")


    def __pow__(self, power, modulo=None):
        if type(power) is Roman:
            return Roman(self.val ** power.val)

        elif type(power) is int:
                return Roman(self.val ** power)

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")

    def __rpow__(self, other):
        if type(other) is Roman:
            return Roman(other.val ** self.val)

        elif type(other) is int:
            return Roman(other ** self.val)

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")


    def __eq__(self, other):
        if type(other) is Roman:
            return self.val == other.val

        elif type(other) is int:
            return self.val == other

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")

    def __ne__(self, other):
        if type(other) is Roman:
            return self.val != other.val

        elif type(other) is int:
            return self.val != other

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")

    def __lt__(self, other):
        if type(other) is Roman:
              return self.val < other.val

        elif type(other) is int:
            return self.val < other

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")

    def __gt__(self, other):
        if type(other) is Roman:
              return self.val > other.val

        elif type(other) is int:
            return self.val > other

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")

    def __le__(self, other):
        if type(other) is Roman:
              return self.val <= other.val

        elif type(other) is int:
            return self.val <= other

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")

    def __ge__(self, other):
        if type(other) is Roman:
              return self.val >= other.val

        elif type(other) is int:
            return self.val >= other

        else:
            raise TypeError("Roman objects can only interact with an integer or Roman")

    def __neg__(self):
        return Roman(-self.val)


#converts value to a roman numeral
def toR(n):

    dictRoman = OrderedDict()

    s = ""

    dictRoman[1]    = "I"
    dictRoman[4]    = "IV"
    dictRoman[5]    = "V"
    dictRoman[9]   = "IX"
    dictRoman[10]   = "X"
    dictRoman[40]   = "XL"
    dictRoman[50]   = "L"
    dictRoman[90]   = "XC"
    dictRoman[100]  = "C"
    dictRoman[400]  = "CD"
    dictRoman[500]  = "D"
    dictRoman[900]  = "CM"
    dictRoman[1000] = "M"

    if n == 0:
        return "N"

    if n < 0:
        s = "-"
        n = -n

    for k in reversed(dictRoman.keys()):
        if (k * 1000) <= n and n >= 4000:
            q = n // (k * 1000)
            n -= q * (k * 1000)

            if dictRoman[k] == "IV":
                s += q * ("M(V)")
            elif dictRoman[k] == "IX":
                s += q * ("M(X)")
            else:
                s += q * ("(" + dictRoman[k] + ")")


    for k in reversed(dictRoman.keys()):
        if k <= n:
            q = n // k
            n -= q * k
            s += q * dictRoman[k]

    return s


#create all of the roman objects
for x in range(0, 1001):
    globals()[toR(x)] = Roman(x)