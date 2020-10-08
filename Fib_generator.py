import functools
from time import sleep, time


def measure(func):
    """Check execution time of a given function
        Returns:
        _time_it: Total execution time in nanoseconds(1/1000000000 os a second)
    """
    @functools.wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000000000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000000000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ns")

       
    return _time_it


@measure
def fibonacci(n: int):
    """Fibonacci numbers generator, yield first n + 1 numbers

    Args:
        n ([int]): [count of first numbers]
    """
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a 
        a, b = b, a + b
        counter += 1
        
f = fibonacci(10)

for x in f:
    print(x)
    
print(measure.__doc__)
print(fibonacci.__doc__)