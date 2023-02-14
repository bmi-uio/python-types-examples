from pydantic import BaseModel


def add(a: int, b: int) -> int:
    return a + b


asdasd = add(123, 234)
str_b = add('sdfs', 'sdf')
print(str_b)

mystuff: list[int] = ['34', 123, 'asd', True]


class ListIntModel(BaseModel):
    mystuff: list[int]


abc = ListIntModel(mystuff=['34', 123, '2345', True])
dfg: int = int('23')

print(abc.mystuff)
