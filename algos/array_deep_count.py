#import dis
import cProfile


def deep_count(a):
    total = 0
    for item in a:
        total += 1
        if isinstance(item, list):
            total += deep_count(item)
    return total


cProfile.run('deep_count([1, 2, [3, 4, [5]]])')
# dis.dis(deep_count)
