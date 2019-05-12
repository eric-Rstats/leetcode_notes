# 使用队列实现层次遍历


class Nodes():

    def __init__(self, index=-1, left=-1, right=-1):
        self.index = index
        self.left = left
        self.right = right

    def is_empty(self):
        return self.index == -1

    def is_leaves(self):
        """判断是否叶子节点
        """
        return self.left == self.right == -1

    def add_queue(self, queue):
        queue


# 读取数据
def read():
    size = int(input())  # 树的结点个数
    if size == 0:
        return [], -1
    tree = []
    is_root = [1 for i in range(size)]
    for i in range(size):
        left, right = input().split()

        if left == '-':
            left = -1
        else:
            left = int(left)
            is_root[left] = 0

        if right == '-':
            right = -1
        else:
            right = int(right)
            is_root[right] = 0

        tree.append(Nodes(i, left, right))

    for i in range(size):
        if is_root[i] == 1:
            break

    return tree, i  # 分别返回tree和root所在的index

# 层次遍历


def bianli(tree, root):
    """层次遍历
    """

    if root == -1:
        # 如果树为空
        result = '-'
    else:
        d, result = [], []
        d.append(root)
        while len(d) > 0:
            current = d.pop()
            # 获取当前元素
            if tree[current].is_leaves():  # 如果是叶子节点，输出
                result.append(current)

            else:
                left = tree[current].left
                right = tree[current].right

                if left != -1:
                    d.insert(0, left)
                if right != -1:
                    d.insert(0, right)

    return result


t, root = read()
result = bianli(t, root)
for i in range(len(result)):
    if i == 0:
        print(str(result[i]), end='')
    else:
        print('', str(result[i]), end='')
