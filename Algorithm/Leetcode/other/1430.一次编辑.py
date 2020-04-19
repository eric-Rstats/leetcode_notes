class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m = len(first)
        n = len(second)

        if m < n:
            first, second = second, first
            m, n = n, m

        if m-n > 1:
            return False

        for i in range(n):
            if first[i] != second[i]:
                return first[i+1:] == second[i+1:] or first[i+1:] == second[i:]

        return True
