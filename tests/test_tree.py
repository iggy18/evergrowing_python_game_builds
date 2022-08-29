import pytest

from ..datastructure.tree import Tree

def test_binary_tree_init():
    tree = Tree()
    assert tree
    
def test_binary_tree_insert():
    tree = Tree()
    tree.insert(1)
    assert tree.root.value == 1
    
def test_binary_tree_insert_with_left_child():
    tree = Tree()
    tree.insert(1)
    tree.insert(2)
    assert tree.root.value == 1
    assert tree.root.left.value == 2
    
def test_binary_tree_insert_with_left_and_right_child():
    tree = Tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    assert tree.root.value == 1
    assert tree.root.left.value == 2
    assert tree.root.right.value == 3
    
def test_binary_tree_insert_with_multiple_levels():
    tree = Tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    assert tree.root.value == 1
    assert tree.root.left.value == 2
    assert tree.root.right.value == 3
    assert tree.root.left.left.value == 4
    assert tree.root.left.right.value == 5
    
def test_depth_first_traversal():
    tree = Tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    assert tree.depth_first_traversal_itter() == [1, 2, 3, 4, 5]