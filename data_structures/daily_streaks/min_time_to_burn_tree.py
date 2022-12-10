"""
Given a binary tree and a leaf node from this tree. It is known that in 1s all nodes connected to a given node,
(left child, right child, and parent) get burned in 1 second. Then all the nodes which are connected through
one intermediate get burned in 2 seconds, and so on.
The task is to find the minimum time required to burn the complete binary tree.
"""

from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.data = val


class Solution:
    def minTime(self, root, target):
        parent = {}
        self.bfs_traversal(root, parent)

        visited = set()
        queue = deque()
        queue.append(target)
        visited.add(target)
        print([target])
        min_time = -1
        while queue:
            len_q = len(queue)
            temp = []
            while len_q != 0:
                pop = queue.popleft()
                node = parent[pop]["node"]
                parent_node = parent[pop]["parent"]
                len_q -= 1
                if parent_node is not None:
                    if parent_node.data not in visited:
                        queue.append(parent_node.data)
                        visited.add(parent_node.data)
                        temp.append(parent_node.data)
                if node.left:
                    if node.left.data not in visited:
                        queue.append(node.left.data)
                        visited.add(node.left.data)
                        temp.append(node.left.data)
                if node.right:
                    if node.right.data not in visited:
                        queue.append(node.right.data)
                        visited.add(node.right.data)
                        temp.append(node.right.data)
            print(temp)
            min_time += 1
        return min_time

    def bfs_traversal(self, root, parent):
        queue = deque()
        queue.append(root)
        parent[root.data] = {"parent": None, "node": root}
        while queue:
            len_q = len(queue)
            while len_q != 0:
                pop = queue.popleft()
                len_q -= 1
                if pop.left:
                    parent[pop.left.data] = {"parent": pop, "node": pop.left}
                    queue.append(pop.left)
                if pop.right:
                    parent[pop.right.data] = {"parent": pop, "node": pop.right}
                    queue.append(pop.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(7)
root.left.right.right = Node(8)
root.right.right = Node(6)
root.right.right.right = Node(9)
root.right.right.right.right = Node(10)

# soln = Solution()
# print(soln.minTime(root, 8))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
root.left.right = Node(5)
root.left.right.left = Node(10)
root.right = Node(3)
root.right.right = Node(7)

# soln = Solution()
# print(soln.minTime(root, 10))


root = Node(12)
root.left = Node(13)
root.right = Node(10)
root.right.left = Node(14)
root.right.right = Node(15)
root.right.left.left = Node(21)
root.right.left.right = Node(24)
root.right.right.left = Node(22)
root.right.right.right = Node(23)
soln = Solution()
print(soln.minTime(root, 14))
