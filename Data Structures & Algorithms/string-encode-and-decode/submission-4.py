class Solution:
    arr = []
    def encode(self, strs: List[str]) -> str:
        complete = ""
        for s in strs:
            self.arr.append(len(s))
            complete += s

        return complete

    def decode(self, s: str) -> List[str]:
        words = []
        old = 0
        for new in self.arr:
            print(new)
            words.append(s[old:old + new])
            old += new

        return words

