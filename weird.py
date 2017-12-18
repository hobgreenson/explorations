import sys
import time

import matplotlib.pyplot as plt

sys.setrecursionlimit(10001)

def count_down(n):
    """Dumb recursive function.
    """
    if n == 0: return
    count_down(n-1)


def time_call_overhead():
    """Times the execution of a 
    number (size) of recursive function calls.
    """
    sizes = list(range(895,907))
    times = []
    for size in sizes:
        t = time.time()
        count_down(size)
        times.append(time.time() - t)
    return sizes, times


def main():
    s, t = time_call_overhead()
    fig, ax = plt.subplots(1,1)
    ax.plot(s, t, '-ok')
    ax.set_xlabel('Number of recursive calls')
    ax.set_ylabel('Execution time')
    plt.show()


if __name__ == '__main__':
    main()

