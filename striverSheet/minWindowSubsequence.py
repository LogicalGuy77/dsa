class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n = len(s1)
        m = len(s2)

        ans = ""
        min_len = float("inf")

        i = 0

        while i < n:
            # Forward scan: find s2 as a subsequence
            j = 0

            while i < n:
                if s1[i] == s2[j]:
                    j += 1

                    if j == m:
                        break

                i += 1

            # No more subsequences possible
            if j < m:
                break

            # Backward scan: minimize this window
            end = i
            j = m - 1

            while j >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                i -= 1

            start = i + 1

            if end - start + 1 < min_len:
                min_len = end - start + 1
                ans = s1[start:end + 1]

            # Start looking for the next window
            i = start + 1

        return ans


s1 =  "jmeqsiwvaovvnbstl"
s2 = "u"
obj = Solution()
print(obj.minWindow(s1, s2))