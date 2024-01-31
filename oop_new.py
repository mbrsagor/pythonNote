from typing import override


class Parent(object):
    def foo(self, x: int) -> int:
        return x


class Child(Parent):
    @override
    def foo(self, x: int) -> int:
        return x + 1


def parent_callsite(parent: Parent) -> None:
    parent.foo(1)


def child_callsite(child: Child) -> None:
    child.foo(1)  # Type checker ensures correct override
