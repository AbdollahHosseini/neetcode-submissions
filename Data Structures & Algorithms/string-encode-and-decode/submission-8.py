class Solution:
    arr = []
    def encode(self, strs: List[str]) -> str:
        complete = ""
        for s in strs:
            self.arr.append(len(s))
            print(len(s))
            complete += s

        print(complete, print(self.arr))
        return complete

    def decode(self, s: str) -> List[str]:
        words = []
        old = 0
        for new in self.arr:
            words.append(s[old:old + new])
            self.arr.pop(0)
            old += new

        return words

