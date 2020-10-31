class Operator:
    def __init__(self, num_in, num_out, fn):
        self.num_in = num_in
        self.num_out = num_out
        self.fn = fn

    def __call__(self, stack):
        args = stack.pop_n(self.num_in)
        res = self.fn(*args)
        stack.push_n(self.num_out, res)
