class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return set(sorted(Counter(s).items()))==set(sorted(Counter(t).items())) and len(s)==len(t)
        