from typing import override

class Base:
    def method(self): pass

class Sub(Base):
    @override
    def method(self): pass

