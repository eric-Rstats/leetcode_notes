# 1. 先构建树, 前序遍历的路径就是push的先后顺序
# 2. 再后序遍历这棵树

# 定义node


class Node:

    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self, root=None):
        self.root = root

    def postorder(self, root):
        """后序遍历"""

# 定义函数从先序遍历的路径里面构建树


def build():

    return root


def main():
    # 读取

    bt = build()
    bt.postorder(bt.root)
