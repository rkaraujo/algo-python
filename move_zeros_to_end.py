# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#
# move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]

def move_zeros(array):
    zero_indexes = []

    for index, element in enumerate(array):
        if element is not False and element == 0:
            zero_indexes.append(index)

    removed = 0
    for zero_index in zero_indexes:
        array.pop(zero_index - removed)
        removed += 1

    array = array + [0] * removed

    return array


if __name__ == '__main__':
    assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
    assert move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]) == [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
    assert move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]) == ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
    assert move_zeros([0,1,None,2,False,1,0]) == [1,None,2,False,1,0,0]
    assert move_zeros(["a", "b"]) == ["a", "b"]
    assert move_zeros(["a"]) == ["a"]
    assert move_zeros([0, 0]) == [0, 0]
    assert move_zeros([0]) == [0]
    assert move_zeros([False]) == [False]
    assert move_zeros([]) == []

