from datastruct.BinaryTree import Node


def traverse(root):
    if root is None:
        return
    # 前序位置
    print(f"前序位置: {root.value}")
    traverse(root.left)
    # 中序位置
    print(f"中序位置: {root.value}")
    traverse(root.right)
    print(f"后序位置: {root.value}")
    # 后序位置


def max_depth(root):
    # 记录最大深度
    res = 0
    # 记录遍历到的节点的深度
    depth = 0

    def traverse(root):
        nonlocal res
        nonlocal depth
        if not root:
            return
        # 前序位置
        depth += 1
        if not root.left and not root.right:
            # 到达叶子节点，更新最大深度
            res = max(res, depth)
        traverse(root.left)
        traverse(root.right)
        # 后序位置
        depth -= 1

    traverse(root)
    return res


def maxDepth(root):
    if root is None:
        return 0
    left_max = maxDepth(root.left)
    right_max = maxDepth(root.right)
    return max(left_max, right_max) + 1


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    traverse(root)
    print(f"max_depth: {max_depth(root)}, maxDepth: {maxDepth(root)}")
