class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        p1 = m-1   # A的左指针
        p2 = n-1  # B的右指针
        p = m+n-1  # 最终合并列表的右指针

        while p1 >= 0 and p2 >= 0:
            if A[p1] < B[p2]:
                # 如果当前p1指向元素小于p2指向元素
                A[p] = B[p2]
                p2 -= 1
                p -= 1
            else:
                A[p] = A[p1]
                p1 -= 1
                p -= 1

        A[:p2+1] = B[:p2+1]
        return A
