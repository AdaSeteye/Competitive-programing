class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            temp = self.getRow(rowIndex - 1)
            row = [1]
            for i in range(len(temp) - 1):
                row.append(temp[i]+ temp[i + 1])
            row.append(1)
            return row
