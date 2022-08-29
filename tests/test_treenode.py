import pytest

from ..datastructure.tree_node import TreeNode

def test_tree_node_init():
    node = TreeNode()
    assert node
    
def test_tree_node_with_value():
    node = TreeNode(1)
    assert node.value == 1
    
def test_tree_node_with_value_and_left_child_without_value():
    node = TreeNode(1)
    left_child = TreeNode()
    node.left = left_child
    assert node.left.value == None
    assert node.left == left_child
    
def test_tree_node_with_value_and_right_child_without_value():
    node = TreeNode(1)
    right_child = TreeNode()
    node.right = right_child
    assert node.right.value == None
    assert node.right == right_child
    
def test_tree_node_with_value_and_left_and_right_child_without_value():
    node = TreeNode(1)
    left_child = TreeNode()
    right_child = TreeNode()
    node.left = left_child
    node.right = right_child
    assert node.value == 1
    assert node.left == left_child
    assert node.right == right_child
    assert node.left.value == None
    assert node.right.value == None
    
def test_tree_node_with_value_and_left_child_with_value():
    node = TreeNode(1)
    left_child = TreeNode(2)
    right_child = TreeNode(3)
    node.left = left_child
    node.right = right_child
    assert node.value == 1
    assert node.left == left_child
    assert node.left.value == 2
    assert node.right == right_child
    assert node.right.value == 3

