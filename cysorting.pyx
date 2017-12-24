from cython cimport boundscheck, wraparound

def insertion_sort(list x, reverse=False):
    """ Sorts the input array x in either ascending (default)
    or descending order using the insertion sort algorithm.
        Based on CLRS chapter 2.1
    """
    cdef:
        long i
        long j
        long n = len(x)
    for i in range(n):
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


def merge_asc(list left, list right):
    """ Helper function for merge_sort.
    """
    cdef:
        long sl = len(left)
        long sr = len(right)
        long n = sl + sr
        long i = 0
        long j = 0
        list merged = [None] * n
    for k in range(n):
        if i < sl and (j >= sr or left[i] < right[j]):
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
    return merged


def merge_desc(list left, list right):
    """ Helper function for merge_sort.
    """
    cdef:
        long sl = len(left)
        long sr = len(right)
        long n = sl + sr
        long i = 0
        long j = 0
        list merged = [None] * n
    for k in range(n):
        if i < sl and (j >= sr or left[i] > right[j]):
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
    if len(x) <= 75:
        return insertion_sort(x, reverse=reverse)
    if reverse:
        merge = merge_desc
    else:
        merge = merge_asc
    mid = len(x) // 2
    left = merge_sort(x[:mid], reverse=reverse)
    right = merge_sort(x[mid:], reverse=reverse)
    return merge(left, right)

