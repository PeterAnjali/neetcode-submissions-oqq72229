class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = defaultdict(list)
        for x in strs:
            key = tuple(sorted(x))
            lists[key].append(x)
        return list(lists.values())
