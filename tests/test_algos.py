import pytest
from algos import merge_sort, fisher_yates_shuffle

def test_merge_sort():
   
    assert merge_sort([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert merge_sort([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert merge_sort([1, 2, 3]) == [3, 2, 1]
    assert merge_sort([0,0,0,0,0,1,1,1,0,0,0,2,1,1,1,1,0,0,0]) == [2,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
    assert merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert merge_sort([1, 2, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4, 3, 2, 1]

# fisher_yates_shuffle not tested because it is random

if __name__ == "__main__":
    pytest.main(["-v", __file__])