class Solution:
    def encode(self, strs: List[str]) -> str:
        complete = ""
        for s in strs:
            complete += str(len(s)) + "#" + s
        return complete

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)

