"""
Given three inputs all of which are instances of an AncestralTree class that have an ancestor property pointing to their youngest
ancestor.
TopAncestor has no ancestor and points to None.

Hint:- Check the depth of two descendants, and if they are different try to level both the same.
From that point onwards check for their ancestors.

"""


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    depth_one = depth_descendant(topAncestor, descendantOne)
    depth_two = depth_descendant(topAncestor, descendantTwo)

    if depth_one == depth_two:
        yca = get_yca(descendantOne, descendantTwo)
    elif depth_one > depth_two:
        same_level_node = get_same_level_node(depth_one - depth_two, descendantOne)
        yca = get_yca(same_level_node, descendantTwo)
    else:
        same_level_node = get_same_level_node(depth_two - depth_one, descendantTwo)
        yca = get_yca(same_level_node, descendantOne)

    return yca


def depth_descendant(top, desc):
    if desc is None:
        return 0
    return 1 + depth_descendant(top, desc.ancestor)


def get_same_level_node(dec_depth, node):
    if dec_depth == 0 or node.ancestor is None:
        return node
    return get_same_level_node(dec_depth - 1, node.ancestor)


def get_yca(one, two):
    if one == two:
        return one
    return get_yca(one.ancestor, two.ancestor)


def getYoungestCommonAncestorEfficient(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    depth_one = get_depth_descendantEfficient(descendantOne)
    depth_two = get_depth_descendantEfficient(descendantTwo)

    if depth_one > depth_two:
        yca = get_youngest_common_ancestorEfficient(depth_one - depth_two, descendantOne, descendantTwo)
    else:
        yca = get_youngest_common_ancestorEfficient(depth_two - depth_one, descendantTwo, descendantOne)

    return yca


def get_depth_descendantEfficient(desc):
    if desc is None:
        return 0
    return 1 + get_depth_descendantEfficient(desc.ancestor)


def get_youngest_common_ancestorEfficient(depth, one, two):
    if one == two:
        return one
    if depth != 0:
        return get_youngest_common_ancestorEfficient(depth - 1, one.ancestor, two)
    return get_youngest_common_ancestorEfficient(depth, one.ancestor, two.ancestor)
