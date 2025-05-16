"""

Test driven development:


Example from Coding Bat: List-2 > sum13

https://codingbat.com/prob/p167025

Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
sum13([1, 2, 13, 2, 1, 13]) → 4
sum13([13, 1, 2, 13, 2, 1, 13]) → 3
sum13([]) → 0
sum13([13]) → 0
sum13([13, 13]) → 0
sum13([13, 0, 13]) → 0
sum13([13, 1, 13]) → 0
sum13([5, 7, 2]) → 14
sum13([5, 13, 2]) → 5
sum13([0]) → 0
sum13([13, 0]) → 0 
"""

import pytest

# def sum13(nums):
#     """
#     non-functional -- but the tests will run (and fail)
#     """
#     return None

# def sum13(nums):
#     """
#     simple sum -- no special handling of 13 -- should pass some tests.
#     """
#     return sum(nums)


# def sum13(nums):
#     """
#     using a comprehension to filter out the 13s

#     - more tests should pass, but not all.
#     """
#     return sum(n for n in nums if n!=13)


# def sum13(nums):
#     """
#     darn -- comprehension can't handle the "after a 13" case

#     do it from scratch with  while loop

#     fails the two 13s in a row test!
#     """
#     total = 0
#     i = 0
#     while i < len(nums):
#         if nums[i] != 13:
#             total += nums[i]
#         else:
#             i += 1
#         i += 1
#     return total


# def sum13(nums):
#     """
#     Use a for loop, and keep track of the previous 13

#     passes all tests!
#     """
#     print(nums)
#     total = 0
#     prev_13 = False
#     for i, n in enumerate(nums):
#         if n == 13:
#             prev_13 = True
#             continue
#         elif prev_13:
#             prev_13 = False
#             continue
#         else:
#             total += n
#     return total


def sum13(nums):
    """
    Use the iterator protocol -- nifty? but not any simpler really.

    Fails for repeated 13 in middle

    Works with any iterable, so that's nice.
    """
    total = 0
    nums_i = iter(nums)
    for n in nums_i:
        if n != 13:
            total += n
        else:
            try:
                next(nums_i)
            # this is necessary for the case where there's a 13 at the end.
            except StopIteration:
                break
    return total

# Using the nifty pytest.parametrize, so we only have to write one test

test_data = [
    ([1, 2, 2, 1], 6),
    ([1, 1], 2),
    ([1, 2, 2, 1, 13], 6),
    ([1, 2, 2, 1], 6),
    ([1, 1], 2),
    ([1, 2, 2, 1, 13], 6),
    ([1, 2, 13, 2, 1, 13], 4),
    ([13, 1, 2, 13, 2, 1, 13], 3),
    ([], 0),
    ([13], 0),
    ([13, 13], 0),
    ([13, 0, 13], 0),
    ([13, 1, 13], 0),
    ([5, 7, 2], 14),
    ([5, 13, 2], 5),
    ([0], 0),
    ([13, 0], 0),
    # These are not part of original test suite
    # ([3, 13, 13, 2, 5], 8),
    # (iter([13, 1, 2, 13, 2, 1, 13]), 3), #  Does it work with an iterable?
    ]

@pytest.mark.parametrize('nums, result', test_data)
def test_sum13(nums, result):
    assert sum13(nums) == result



                              
