'''
Test script for linked list hw
'''

from ku_submission import Node, DLL

def test_DLL_Class():
    '''
    Create a DLL with the following elements (in order)
    [1 <-> 2 <-> 3 <-> 4]
    and tests the following:
    Attributes: head, tail, prev, next
    Methods: length(), index(), push(), insert(), delete(),
    multiply_all_pairs()
    '''

    # Create empty list
    test_DLL = DLL()
    assert test_DLL.length() == 0
    assert test_DLL.multiply_all_pairs() == 0

    # DLL = 4
    test_DLL.push(4)
    assert test_DLL.length() == 1
    assert test_DLL.head.val == 4
    assert test_DLL.tail.val == 4

    # DLL = 2 <-> 4
    test_DLL.push(2)
    head_node = test_DLL.head

    # DLL = 2 <-> 3 <-> 4
    test_DLL.insert(3, head_node)
    assert test_DLL.length() == 3
    assert test_DLL.multiply_all_pairs() == 26
    second_node = test_DLL.head.next
    assert head_node.next == second_node
    assert second_node.prev == head_node

    # DLL = 1 <-> 2 <-> 3 <-> 4
    test_DLL.push(1)
    assert test_DLL.length() == 4
    assert test_DLL.multiply_all_pairs() == 35
    assert test_DLL.tail.val == 4
    assert test_DLL.index(0).val == 1
    assert test_DLL.index(1).val == 2
    assert test_DLL.index(2).val == 3
    assert test_DLL.index(3).val == 4

    # DLL = 1 <-> 2 <-> 4
    test_DLL.delete(test_DLL.tail.prev)
    assert test_DLL.tail.prev == test_DLL.head.next
    assert test_DLL.length() == 3

    # DLL = 2 <-> 4
    test_DLL.delete(test_DLL.head)
    assert test_DLL.tail.val == 4

    # DLL = 2
    test_DLL.delete(test_DLL.tail)
    assert test_DLL.head == test_DLL.tail
    assert test_DLL.head.val == 2
