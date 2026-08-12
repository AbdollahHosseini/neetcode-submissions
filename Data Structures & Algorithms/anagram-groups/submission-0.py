class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        if len(strs) <= 1:
            return [strs]

        seen = []
        for x in range(len(strs)):
            similar = []
            curr = strs[x]
            if x < len(strs) and curr not in seen:
                similar.append(curr)
                seen.append(curr)
                for y in range(x+1, len(strs)):
                    if sorted(strs[y]) == sorted(curr):
                        similar.append(strs[y])
                        seen.append(strs[y])
            
                result.append(similar)

        return result
