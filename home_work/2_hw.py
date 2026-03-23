def task_1() -> None:
    a: int = 10
    b: float = 2.5
    c: str = "apple"
    d: list = [3, "banana", 3.14]
    e: bool = True

    print(f"a = {type(a)}")
    print(f"b = {type(b)}")
    print(f"c = {type(c)}")
    print(f"d = {type(d)}")
    print(f"e = {type(e)}")

task_1()


def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]  # список
    print(a[:3])

task_2()


def task_3(n: int) -> int:
    return n ** 2

print(task_3(5))