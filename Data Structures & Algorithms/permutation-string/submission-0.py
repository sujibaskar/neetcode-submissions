class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        have = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1

        s = 0  # start pointer

        for e in range(len(s2)):
            c = s2[e]

            # If character not needed, reset window
            if c not in need:
                have.clear()
                s = e + 1
                continue

            have[c] = have.get(c, 0) + 1

            # Shrink window if count exceeds
            while have[c] > need[c]:
                s_char = s2[s]
                have[s_char] -= 1
                s += 1

            # Check window size
            if e - s + 1 == len(s1):
                return True

        return False
