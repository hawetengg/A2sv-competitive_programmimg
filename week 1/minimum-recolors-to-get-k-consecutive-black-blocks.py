class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = []
        count = blocks[:k].count("W")
        ans.append(count)

        for i in range(1, len(blocks) - k + 1):
            if blocks[i - 1 + k] == "W":
                count += 1
            if blocks[i - 1] == "W":
                count -= 1
            ans.append(count)
        minn = min(ans)
        return minn
        