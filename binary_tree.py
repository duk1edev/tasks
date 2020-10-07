# from extratypes import Tree  # library with types used in the task


def solution(T):
    if not T:
        return 0
    return count_visible_nodes(T, float('-inf'))


def count_visible_nodes(node, max_value):
    if not node:
        return 0
    visible = 1 if node.x >= max_value else 0
    max_value = max(max_value, node.x)
    return count_visible_nodes(node.l, max_value) + visible + count_visible_nodes(node.r, max_value)


def count_all_nodes(T):
    if T is None:
      return 0
    if T.x is not None:
        return 1 + solution(T.l) + solution(T.r)
