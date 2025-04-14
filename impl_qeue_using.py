class MyQueue(object):
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """pushes"""
        self.stack_in.append(x)

    def pop(self):
        """pops"""
        self._transfer()
        return self.stack_out.pop()

    def peek(self):
        '''peeks'''
        self._transfer()
        return self.stack_out[-1]

    def empty(self):
        """empty"""
        return not self.stack_in and not self.stack_out

    def _transfer(self):
        """trasfers"""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
