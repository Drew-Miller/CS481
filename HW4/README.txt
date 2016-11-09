I did the extra credit where you can add more than two particles and
create a tuple of particles to pass into a reaction.

def __add__(self, other):
    if type(other) is tuple:
        return (self,) + other

    elif type(other) is Particle:
        return (self, other)

def __radd__(self, other):
    return self + other
