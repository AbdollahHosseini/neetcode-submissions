class Solution:
    arr = []
    def encode(self, strs: List[str]) -> str:
        complete = ""
        for i in strs:
            self.arr.append(len(i))
            complete += i
        return complete


    def decode(self, s: str) -> List[str]:
        strs = []
        old = 0
        for num in self.arr:
            curr = s[old:old+num]            
            strs.append(curr)
            old += num
        return strs