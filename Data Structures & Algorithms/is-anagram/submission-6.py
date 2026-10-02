class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        track1 = {}
        track2 = {}
        for i in range(len(s)):
            if s[i] not in track1:
                track1[s[i]] = 1
            else:
                track1[s[i]] += 1
            if t[i] not in track2:
                track2[t[i]] = 1
            else:
                track2[t[i]] += 1
        return track1 == track2