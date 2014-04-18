

def mergesort(seq, in_place=True):
    """Sorts `seq` using the mergesort algorithm.

    `seq` is the sequence to be sorted. If `in_place` is `True`
    the sequence itself will be sorted and returned, else a copy
    of the original sequence is used.
    """
    seq = seq if in_place else seq[:]
    _mergesort(seq, 0, len(seq) - 1)
    return seq


def straight_mergesort(seq, in_place=True):
    """Sorts `seq` using the straight-mergesort algorithm.

    `seq` is the sequence to be sorted. If `in_place` is `True`
    the sequence itself will be sorted and returned, else a copy
    of the original sequence is used.
    """
    seq = seq if in_place else seq[:]
    size, length = 1, len(seq)
    while size <= length:
        right = -1
        while right + size < length:
            left = right + 1
            mid = left + size - 1
            right = mid + size if mid + size < length else length - 1
            _merge(seq, left, mid, right)
        size *= 2
    return seq


def _mergesort(seq, left, right):
    if not left < right:
        return
    mid = (left + right) // 2
    _mergesort(seq, left, mid)
    _mergesort(seq, mid + 1, right)
    _merge(seq, left, mid, right)


def _merge(seq, left, mid, right):
    result = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if seq[i] <= seq[j]:
            result.append(seq[i])
            i += 1
        else:
            result.append(seq[j])
            j += 1
    if i > mid:
        result += seq[j:right + 1]
    else:
        result += seq[i:mid + 1]
    seq[left:right + 1] = result


def quicksort(seq, in_place=True):
    """Sorts `seq` using the quicksort algorithm.

    `seq` is the sequence to be sorted. If `in_place` is `True`
    the sequence itself will be sorted and returned, else a copy
    of the original sequence is used.
    """
    seq = seq if in_place else seq[:]
    _quicksort(seq, 0, len(seq) - 1)
    return seq


def _quicksort(seq, left, right):
    if left >= right:
        return

    pivot = seq[right]
    i, j = left, right

    while True:
        while seq[i] <= pivot and i < right:
            i += 1
        while seq[j] >= pivot and j > i:
            j -= 1
        if i >= j:
            break
        _swap(seq, i, j)
    _swap(seq, i, right)

    _quicksort(seq, left, i - 1)
    _quicksort(seq, i + 1, right)


def bubblesort(seq, in_place=True):
    """Sorts `seq` using the bubblesort algorithm.

    `seq` is the sequence to be sorted. If `in_place` is `True`
    the sequence itself will be sorted and returned, else a copy
    of the original sequence is used.
    """
    seq = seq if in_place else seq[:]
    for n in range(len(seq), 1, -1):
        swapped = False
        for i in range(n - 1):
            if seq[i] > seq[i + 1]:
                _swap(seq, i, i + 1)
                swapped = True
        if not swapped:
            break
    return seq


def _swap(seq, first, second):
    seq[first], seq[second] = seq[second], seq[first]
