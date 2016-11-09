#!/usr/bin/env python3

class Particle:
    def __init__(self, name, charge, mass):
        self.name = name
        self.charge = charge
        self.mass = mass

    def __repr__(self):
            return ("Particle('%s', %d, %d')" %(self.name, self.charge, self.mass))

    def __str__(self):
            return self.name

    def __add__(self, other):
        if type(other) is tuple:
            return (self,) + other

        elif type(other) is Particle:
            return (self, other)

    def __radd__(self, other):
        return self + other


class Nucleus(Particle):
        def __init__(self, name, charge, mass):
            super(Nucleus, self).__init__(name, charge, mass)

        def __repr__(self):
            return ("Nucleus('%s', %d, %d')" %(self.name, self.charge, self.mass))

        def __str__(self):
            return ("(%d)%s" % (self.mass, self.name))



class Reaction:
    def __init__(self, left, right):
        lc = 0
        lm = 0
        rc = 0
        rm = 0

        self.left = left
        self.right = right

        for p in left:
            lc += p.charge
            lm += p.mass

        for p in right:
            rc += p.charge
            rm += p.mass

        if lc != rc:
            raise UnbalancedCharge(lc - rc)

        if lm != rm:
            raise UnbalancedMass(lm - rm)

    def __str__(self):
        total = ""
        for p in self.left:
            total += str(p)
            total += " + "

        total = total[:-3]
        total += " -> "

        for p in self.right:
            total += str(p)
            total += " + "

        total = total[:-3]

        return total

class ChainReaction:
    def __init__(self, name):
        self.name = name + ":"
        self.chain = []

    def __str__(self):
        s = self.name + "\n"

        lhsNet = []
        rhsNet = []

        for r in self.chain:
            s = s + str(r) + "\n"
            for p in r.left:
                lhsNet.append(p)

            for p in r.right:
                rhsNet.append(p)

        s = s + "net:\n"

        #do removal of net here
        remove = []
        for p in lhsNet:
            print(p + " in both")
            if p in rhsNet:
                rhsNet.remove(p)
                remove.append(p)

        for p in remove:
            lhsNet.remove(p)

        hasLeft = False
        for p in lhsNet:
            hasLeft = True
            s = s + str(p)
            s = s + " + "

        if hasLeft:
            s = s[:-3]

        s = s + "-> "

        hasRight = False
        for p in rhsNet:
            hasRight = True
            s = s + str(p)
            s = s + " + "

        if hasRight:
            s = s[:-3]

        return s

    def addReaction(self, reaction):
        self.chain.append(reaction)


class UnbalancedCharge(Exception):
    def __init__(self, args):
        super(UnbalancedCharge, self).__init__("UnbalancedCharge Exception {0}".format(str(args)))

class UnbalancedMass(Exception):
    def __init__(self, args):
        super(UnbalancedMass, self).__init__("UnbalancedMass Exception {0}".format(str(args)))

if __name__ == "__main__":
    chnPP = ChainReaction("proton-proton (branch I)")
    li6 = Nucleus("Li", 0, 6)
    p = Particle("p", 1, 0)
    e = Particle("e", -1, 0)
    d = Particle("H", 1, 2)
    neut = Particle("N", 0, 0)

    print("EMPTY CHAIN:\n" +
        str(chnPP) + "\n\n" +
        "LI6 NUECLEUS:\n" + str(li6) + "\n\n" +
        "P PARTICLE\n" + str(p) + "\n\n" +
        "E PARTICLE\n" + str(e) + "\n\n" +
        "D PARTICLE" + str(d) + "\n")

    r1 = Reaction(e + p, neut + neut)
    r2 = Reaction((li6,), d + d + d + e + e + e)

    print("REACTION1\n" + str(r1))
    print("REACTION2\n" + str(r2))

    chnPP.addReaction(r1)
    chnPP.addReaction(r2)

    print("CHAINPP:\n" + str(chnPP))
