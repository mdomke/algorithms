from __future__ import print_function
import random
import pytest


def mergesort(seq, in_place=True):
    """Sorts `seq` using the mergesort algorithm.

    `seq` is the sequence to be sorted. If `in_place` is `True`
    the sort will be performed in situ, else a new sorted sequence
    will be returned.
    """
    seq = seq if in_place else seq[:]
    _mergesort(seq, 0, len(seq) - 1)
    return seq


def straight_mergesort(seq, in_place=True):
    """Sorts `seq` using the straight-mergesort algorithm.

    `seq` is the sequence to be sorted. If `in_place` is `True`
    the sort will be performed in situ, else a new sorted sequence
    will be returned.
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
    the sort will be performed in situ, else a new sorted sequence
    will be returned.
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
        seq[i], seq[j] = seq[j], seq[i]
    seq[i], seq[right] = seq[right], seq[i]

    _quicksort(seq, left, i - 1)
    _quicksort(seq, i + 1, right)


@pytest.fixture
def seq():
    return random.sample(range(10 ** 2), 10)


def test_quicksort(seq):
    assert_sorted(quicksort(seq, in_place=False))


def test_mergesort(seq):
    assert_sorted(mergesort(seq, in_place=False))


def assert_sorted(seq):
    length = len(seq)
    if length < 2:
        # Empty and one-element lists are sorted by definition
        return
    for i in range(length - 1):
        assert seq[i] <= seq[i + 1]
