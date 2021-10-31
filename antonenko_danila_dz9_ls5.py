class Stationery:
    title: str

    def draw(self):
        return 'some basic stuff'

class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        return self.title

class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        return self.title

class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        return self.title


p = Pen()
pc = Pencil()
h = Handle()
s = Stationery()

print(s.draw())
print(h.draw())
print(p.draw())
print(pc.draw())