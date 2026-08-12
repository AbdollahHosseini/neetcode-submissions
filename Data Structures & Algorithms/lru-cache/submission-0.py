class Node:
    def __init__(self, val, key, next=-1, prev=-1):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.start = None
        self.end = None
        self.keyRef = {}
        self.count = 0

    def _moveToFront(self, ref):
        if ref == self.start:
            return
        prev = ref.prev
        next = ref.next
        prev.next = next
        if next == -1:
            self.end = prev
        else:
            next.prev = prev
        self.start.prev = ref
        ref.next = self.start
        ref.prev = -1
        self.start = ref

    def get(self, key: int) -> int:
        if key in self.keyRef:
            ref = self.keyRef[key]
            self._moveToFront(ref)
            return ref.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyRef:
            ref = self.keyRef[key]
            ref.val = value
            self._moveToFront(ref)
            return

        ref = Node(value, key)
        if not self.start:
            self.start = ref
            self.end = ref
            self.count += 1
        elif self.count == self.capacity:
            delKey = self.end.key
            self.keyRef.pop(delKey, None)
            prev = self.end.prev
            if prev == -1:
                self.start = ref
                self.end = ref
            else:
                prev.next = -1
                self.end = prev
                ref.next = self.start
                self.start.prev = ref
                self.start = ref
        else:
            ref.next = self.start
            self.start.prev = ref
            self.start = ref
            self.count += 1

        self.keyRef[key] = ref