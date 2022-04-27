"""
Making a parenthetic expression given expression tree.

ex. (((3+1)*4)/((9-5)+2))
"""


class ExpressionTree:
    def __init__(self, tree):
        self._tree = tree

    def __str__(self):
        expressions = []
        self._parenthesize_recur(self._tree.root(), expressions)
        return "".join(expressions)

    def _parenthesize_recur(self, p, pieces):
        if self._tree.is_leaf(p):
            pieces.append(str(p.element()))
        else:
            pieces.append("(")
            self._parenthesize_recur(self._tree.left(p), pieces)
            pieces.append(p.element())
            self._parenthesize_recur(self._tree.right(p), pieces)
            pieces.append(")")


"""
Evaluation of expression tree.

Algorithm evaluate_recur(p):
    if p is leaf:
        return value stored at p
    else:
        op = p.element()
        left = evaluate_recur(left(p))
        right = evaluate_recur(right(p))
        return left op right
"""


def evaluate(self):
    return self._evaluate_recur(self._tree.root())


def _evaluate_recur(self, root):
    if self._tree.is_leaf(root):
        return float(root.element())
    else:
        op = root.element()
        left = self._evaluate_recur(self._tree.left(root))
        right = self._evaluate_recur(self._tree.left(root))

        if op == "+":
            return left + right
        elif op == "-":
            return left - right
        elif op == "*":
            return left * right
        else:
            return left / right


"""Build an expression tree given arithmetic expression."""


def build_expression_tree(self, tokens):
    """Returns an expression tree based upon by a tokenized expression
    ex:- (((3+1)*4)/((9-5)+2))
    """
    stack = []
    for t in tokens:
        if t in "+-/*":
            stack.append(t)
        elif t not in "()":
            stack.append(t)
        elif t == ")":
            right = stack.pop()
            op = stack.pop()
            left = stack.pop()
            root = self._tree._add_root(op)
            self._tree._add_left(root, left)
            self._tree._add_right(root, right)
            stack.append(root)
    return stack.pop()
