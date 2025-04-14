class FreqStack(object):

    def __init__(self):
        self.freq_map = {}
        self.freq_group_map = {}
        self.max_freq = 0

    def push(self, val):
        freq = self.freq_map.get(val, 0) + 1
        self.freq_map[val] = freq
        if freq > self.max_freq:
            self.max_freq = freq
        if freq not in self.freq_group_map:
            self.freq_group_map[freq] = []
        self.freq_group_map[freq].append(val)

    def pop(self):
        val = self.freq_group_map[self.max_freq].pop()
        self.freq_map[val] -= 1
        if not self.freq_group_map[self.max_freq]:
            self.max_freq -= 1
        return val
