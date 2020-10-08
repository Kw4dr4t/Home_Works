import functools
from time import sleep, time


def time_it(func):
    """
    [time_it(func):
    Check execution time of a given function]
    Returns:
    _time_it: Total execution time in nanoseconds(1/1000000000 os a second)
    """
    @functools.wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time()))
        try:
            return func(*args, **kwargs)
        finally:
            end = int(round(time())) - start
            print(f"Total execution time: {end if end > 0 else 0} s")

    return _time_it


@time_it
def countdown(n: int):
    """
    [countdown() -
    Function to countdown given time to zero(launch)]
    Args:
        n (int): [Number to start countdown from it to 0]
    """
    for i in range(n, 0, -1):
        print(f"In {i}")
        sleep(3)
        print("Launch")


countdown(10)
print(time_it.__doc__)
print(countdown.__doc__)