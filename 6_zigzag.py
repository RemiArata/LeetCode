class ZigZag:
    def convert(self, s: str, n: int) -> str:
        rows = [[] for _ in range(n)]
        row_idx = 0
        direction = 1

        for ltr in s:
            rows[row_idx].append(ltr)
            if row_idx + direction == n or row_idx + direction == -1:
                direction *= -1
            row_idx += direction if n > 1 else 0
    
        temp = []
        for arr in rows:
            temp.append("".join(arr))
    
        return "".join(temp)
