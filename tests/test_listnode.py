import pytest

from ..datastructure.list_node import ListNode


def test_list_node_init():
    node = ListNode()
    assert node
    
def test_list_node_with_value():
    node = ListNode(1)
    assert node.value == 1
    
def test_list_node_with_value_and_next_without_value():
    node = ListNode(1)
    next_node = ListNode()
    node.next = next_node
    assert node.value == 1
    assert node.next == next_node
    assert node.next.value == None
