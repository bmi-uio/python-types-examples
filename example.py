from abc import ABC, abstractmethod
from typing import Generic, Protocol, TypeVar, Union

a = Union[str, int]()

b: tuple[int, ...] = (1, 2, 234, 3.4)
c: list[int] = [2, 3, 4]
d: dict[str, int] = {'d': 234}

T = TypeVar('T', int, str)


class CustomQueue(Generic[T]):
    def put(self, task: T) -> None:
        ...

    def get(self) -> T:
        ...


q: CustomQueue[int] = CustomQueue[int]()
#
# def communicate(queue: CustomQueue[str]) -> Optional[str]:
#     ...

l: list[int] = [2.3]


class A(ABC):
    @abstractmethod
    def a(self, i: int) -> int:
        ...


class AA(Protocol):
    def a(self, i: int) -> int:
        ...


class B(A):
    def a(self, i: int) -> int:
        return i + 1

    ...


class BB:
    def a(self, i: int) -> int:
        return i + 1

    ...


def mymethod(x: AA) -> int:
    return x.a(5)


bb = BB()

mymethod(bb)
mymethod(3)
