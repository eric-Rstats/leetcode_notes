
# 定义node


class Node():

    def __init__(self, item=None, left=None, right=None):
        self.item = item  # 值
        self.left = left  # left 指向
        self.right = right  # right 指向

    def is_empty(self):
        return self.item is None


class Tree():

    def __init__(self):
        # 生成一个只有空节点的树
        sefl.root = Node()

    def


def main():
    """主函数
    """

    # 读入结点个数N，和需要比较的树的棵数L
    N, L = [int(x) for x in input().split()]
