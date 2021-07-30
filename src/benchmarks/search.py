import timeit

from src.search.galloping import galloping_search
from src.search.linear import linear_search
from src.search.fibonacci import fibonacci_search
from src.search.binary import binary_search
from src.search.jump import jump_search


BENCH_LIST = list(range(0, 1000000, 7))

bin_time = timeit.timeit(lambda: binary_search(BENCH_LIST, 1337), number=10000)
fib_time = timeit.timeit(lambda: fibonacci_search(BENCH_LIST, 1337), number=10000)
gal_time = timeit.timeit(lambda: galloping_search(BENCH_LIST, 1337), number=10000)
jump_time = timeit.timeit(lambda: jump_search(BENCH_LIST, 1337), number=10000)
lin_time = timeit.timeit(lambda: linear_search(BENCH_LIST, 1337), number=10000)

print(f"Binary avg time: {bin_time / 10000}")
print(f"Fibonacci avg time: {fib_time / 10000}")
print(f"Galloping avg time: {gal_time / 10000}")
print(f"Jump avg time: {jump_time / 10000}")
print(f"Linear avg time: {lin_time / 10000}")
