import asyncio

from memory_profiler import profile


@profile
@asyncio.coroutine
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    yield from asyncio.sleep(1e-2)
    del b
    return 42


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(my_func())
    assert res == 42
