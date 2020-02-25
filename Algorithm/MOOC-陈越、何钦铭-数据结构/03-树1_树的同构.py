
class TreeNode:
    def __init__(self, item=None, left=-1, right=-1):
        """初始化
        """
        self.item = item
        self.left = left
        self.right = right

    def __repr__(self):
        return "Nodes: " + self.item + " left: " + str(self.left) + " right: " + str(self.right)

    def is_empty(self):
        return self.item is None


class BinaryTree:

    def __init__(self):
        self.tree = {}
        self.root = -1

    def build_tree(self):
        size = int(input())
        for i in range(size):
            items = input().split()
            node = TreeNode(items[0], int(items[1]) if items[1] !=
                            '-' else - 1, int(items[2]) if items[2] != '-' else - 1)
            self.tree[i] = node
        # 获取root结点
        if len(self) > 0:
            s = []
            for key, item in self.tree.items():
                if item.left > -1:
                    s.append(item.left)
                if item.right > -1:
                    s.append(item.right)

            a = len(self) * (len(self) - 1) / 2
            b = sum(s)
            self.root = int(a-b)

    def __len__(self):
        return len(self.tree)

    def is_empty(self):
        return len(self.tree) == 0

    def __getitem__(self, index):
        if index == -1:
            return TreeNode()
        else:
            return self.tree[index]


def is_tonggou(t1, t2, r1, r2):
    if r1 == -1 & r2 == -1:
        # 两棵树都为空
        return True
    elif (r1 == -1 and r2 != -1) | (r1 != -1 and r2 == -1):
        # 有一颗树为空
        return False
    elif t1[r1].item != t2[r2].item:
        # 根节点不同
        return False
    elif t1[r1].left == -1 and t2[r2].left == -1:
        # 都没有左子树
        return is_tonggou(t1, t2, t1[r1].right, t2[r2].right)
    elif (t1[r1].left != -1 and t2[r2].left != -1) and (t1[t1[r1].left].item == t2[t2[r2].left].item):
        # 不需要交换左右结点
        return is_tonggou(t1, t2, t1[r1].left, t2[r2].left) and is_tonggou(t1, t2, t1[r1].right, t2[r2].right)
    else:
        # 需要交换左右结点
        return is_tonggou(t1, t2, t1[r1].left, t2[r2].right) and is_tonggou(t1, t2, t1[r1].right, t2[r2].left)


t1 = BinaryTree()
t2 = BinaryTree()
t1.build_tree()
t2.build_tree()
print("Yes" if is_tonggou(t1, t2, t1.root, t2.root) else "No")
