import time

import matplotlib.pyplot as plt


def insertion_sort(x, reverse=False):
    """ Sorts the input array x in either ascending (default)
    or descending order using the insertion sort algorithm.
        Based on CLRS chapter 2.1
    """
    for i in range(1,len(x)):
        elem = x[i]
        j = i - 1
        if reverse:
            while j >= 0 and x[j] < elem:
                x[j+1] = x[j]
                j -= 1
        else:
            while j >= 0 and x[j] > elem:
                x[j+1] = x[j]
                j -= 1
        x[j+1] = elem
    return x


def merge_asc(left, right):
    n = len(left) + len(right)
    merged = [None] * n
    i = j = 0
    for k in range(n):
        if i < len(left) and (j >= len(right) or left[i] < right[j]):
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
    return merged


def merge_desc(left, right):
    n = len(left) + len(right)
    merged = [None] * n
    i = j = 0
    for k in range(n):
        if i < len(left) and (j >= len(right) or left[i] > right[j]):
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
    return merged


def merge_sort(x, reverse=False):
    """ Sorts the input array x in either ascending (default)
    or descending order using the insertion sort algorithm.
        Based on CLRS exercise 2.3-2
    """
    if len(x) <= 1:
        return x
    if reverse:
        merge = merge_desc
    else:
        merge = merge_asc
    mid = len(x) // 2
    left = merge_sort(x[:mid], reverse=reverse)
    right = merge_sort(x[mid:], reverse=reverse)
    return merge(left, right)


def test_sort_algo(sort_func):
    assert sort_func([]) == []
    assert sort_func([3,2,1]) == [1,2,3]
    assert sort_func([1]) == [1]
    assert sort_func([1,2,3]) == [1,2,3]
    assert sort_func([6,1,2,4,10]) == [1,2,4,6,10]
    assert sort_func([1,2,2]) == [1,2,2]
    assert sort_func([6,1,2,4,10], reverse=True) == [10,6,4,2,1]
    assert sort_func([2,-1], reverse=True) == [2,-1]


def time_sort_algo(sort_func):
    sizes = list(range(0,50))
    inputs = []
    times = []
    for size in sizes:
        inputs.append(list(range(size,0,-1)))
    for i in inputs:
        t = time.time()
        sort_func(i)
        times.append(time.time() - t)
    return sizes, times

        
if __name__ == '__main__':
    algorithms = [
        sorted,
        merge_sort,
        insertion_sort,
    ]
    for algo in algorithms:
        test_sort_algo(algo)
    
    colors = ['-ok', '-ob', '-or']
    fig, ax = plt.subplots(1,1)
    for algo, color in zip(algorithms, colors):
        sizes, times = time_sort_algo(algo)
        ax.plot(sizes, times, color)
    ax.set_xlabel('List size')
    ax.set_ylabel('Execution time')
    plt.show()

