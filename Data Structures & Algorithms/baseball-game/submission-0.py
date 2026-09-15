class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # push values to stack
        # O(n) time
        # O(n) space
        record = []
        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])
            elif op == 'C':
                record.pop()
            elif op == 'D':
                record.append(record[-1] * 2)
            else:
                record.append(int(op))
        return sum(record)