# 设计函数分别求两个一元多项式的乘积与和。

# 输入格式:
# 输入分2行，每行分别先给出多项式非零项的个数，再以指数递降方式输入一个多项式非零项系数和指数（绝对值均为不超过1000的整数）。数字间以空格分隔。

# 输出格式:
# 输出分2行，分别以指数递降方式输出乘积多项式以及和多项式非零项的系数和指数。数字间以空格分隔，但结尾不能有多余空格。零多项式应输出0 0。

# 输入样例:
# 4 3 4 - 5 2  6 1 - 2 0
# 3 5 20 - 7 4  3 1
# 输出样例:
# 15 24 - 25 22 30 21 - 10 20 - 21 8 35 6 - 33 5 14 4 - 15 3 18 2 - 6 1
# 5 20 - 4 4 - 5 2 9 1 - 2 0*/


class Nodes:
    """定义结点
    """

    def __init__(self, c=None, p=None):
        self.coef = c
        self.power = p
        self.next = None

    def get_data(self):
        return [self.coef, self.power]

    def __repr__(self):
        return 'Nodes: ' + str(self.coef) + "x^" + str(self.power)

    def is_zero(self):
        """判断node是否为0
        """
        return self.coef == self.power == 0


class Poly:
    def __init__(self):
        self.head = None

    def add_node(self, node):
        """添加一个结点
        """
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def __len__(self):
        """长度函数
        """
        length = 0
        tmp = self.head
        while tmp is not None:
            tmp = tmp.next
            length += 1
        return length

    def __getitem__(self, i):
        """获取某一个位置的元素
        """
        current = self.head
        if i < 0:
            raise ValueError
        else:
            while current != self.rear:
                current = current.next
                i -= 1
            if i > 0:
                raise StandardError
                printZ('Out of index range')
            else:
                return current

    def __repr__(self):
        """定义多项式的输出函数
        """
        if self.head is None:
            return "Nonetype"
        elif self.head.is_zero():
            return "0 0"
        else:
            current = self.head
            result = ''
            while current != None:
                if current.coef != 0:
                    if current == self.head:
                        result = result + \
                            str(current.coef) + ' ' + str(current.power)
                    else:
                        result = result + ' ' + \
                            str(current.coef) + ' ' + str(current.power)
                current = current.next
            return result

    def scan_poly(self, line):
        """从input函数直接返回的字符串构造一个poly列表
        """
        itemlist = [int(i) for i in line.split()]
        size = itemlist[0]

        if size > 0:
            for i in range(1, len(itemlist), 2):
                self.add_node(Nodes(itemlist[i], itemlist[i + 1]))
        elif size == 0:
            self.add_node(Nodes(0, 0))
        else:
            raise IOError

    def __add__(self, p):
        """定义多项式相加的函数
        """
        result = Poly()

        t1 = self.head  # 左边多项式的头结点
        t2 = p.head  # 右边多项式的头结点

        while t1 is not None and t2 is not None:
            if t1.power > t2.power:
                result.add_node(Nodes(t1.coef, t1.power))
                t1 = t1.next
            elif t1.power == t2.power:
                if t1.coef + t2.coef != 0:
                    result.add_node(Nodes(t1.coef + t2.coef, t1.power))
                else:
                    result.add_node(Nodes(0, 0))
                t1 = t1.next
                t2 = t2.next
            else:
                result.add_node(Nodes(t2.coef, t2.power))
                t2 = t2.next

        while t1 is not None:
            result.add_node(Nodes(t1.coef, t1.power))
            t1 = t1.next

        while t2 is not None:
            result.add_node(Nodes(t2.coef, t2.power))
            t2 = t2.next

        return result

    def __mul__(self, p):
        """定义多项式的乘法
        """
        result = Poly()
        t1 = self.head
        t2 = p.head

        if t1.is_zero() or t2.is_zero():
            # 如果任意一个多项式为0，则乘积为0
            result.add_node(Nodes(0, 0))
        else:
            while t2 is not None:
                result.add_node(Nodes(t1.coef * t2.coef, t1.power + t2.power))
                t2 = t2.next

            t1 = t1.next
            while t1 is not None:
                t2 = p.head
                current = result.head
                while t2 is not None:
                    coef = t1.coef * t2.coef
                    power = t1.power + t2.power
                    # 当新的节点小于当前指针所指向的位置，继续往后移动
                    while current.next is not None and power < current.next.power:
                        current = current.next
                    if current.next is not None and current.next.power == power:
                        if coef + current.next.coef == 0:
                            tmp = current.next.next
                            current.next = tmp
                        else:
                            current.next.coef += coef

                    else:
                        # 当前指针所指向位置下一个结点大于power,或者当前指针是最末尾
                        node = Nodes(coef, power)
                        tmp = current.next
                        node.next = tmp
                        current.next = node
                    t2 = t2.next

                t1 = t1.next

        return result


p1 = Poly()
p2 = Poly()
p1.scan_poly(input())
p2.scan_poly(input())
print(p1 * p2)
print(p1 + p2)
