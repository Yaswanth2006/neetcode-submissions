class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = {}
        for i in strs:
            arr = [0] * 26
            for char in i:
                arr[ord(char) - ord('a')] += 1
            key = tuple(arr)
            if key not in track:
                track[key] = [i]
            else:
                track[key].append(i)
        return list(track.values())
