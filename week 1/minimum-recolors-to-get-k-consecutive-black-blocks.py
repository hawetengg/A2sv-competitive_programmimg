class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        look_up = Counter(blocks[:k])
        min_op = look_up["W"]
        l = 0

        for r in range(k, len(blocks)):
            look_up[blocks[r]] += 1
            look_up[blocks[l]] -= 1
            l += 1
            min_op = min(min_op, look_up["W"])
        return min_op
