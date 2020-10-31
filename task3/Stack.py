class Stack(list):
    def pop_n(self, n):
        if n == 0:
            return []
        elif n <= len(self):
            res = self[-n:]
            del self[-n:]
            return res

    def push_n(self, n, items):
        self.extend(items)
