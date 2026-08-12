class Solution:
    arr = []
    def encode(self, strs: List[str]) -> str:
        complete = ""
        for s in strs:
            print(s)
            self.arr.append(len(s))
            complete += s

        print(complete)
        return complete

    def decode(self, s: str) -> List[str]:
        words = []
        old = 0
        for new in self.arr:
            words.append(s[old:old + new])
            old += new

        return words

