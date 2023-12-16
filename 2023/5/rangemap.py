class RangeMap:

    def __init__(self, dest_ranges, source_ranges):
        self.dest_ranges = dest_ranges
        self.source_ranges = source_ranges

    def add_range(self, dest, source):
        self.dest_ranges.append(dest)
        self.source_ranges.append(source)

    def add_from_starts_and_length(self, dest_start, source_start, length):
        self.add_range((dest_start, dest_start + length - 1),
                       (source_start, source_start + length - 1))

    def find_correspondance(self, i):
        interval = self.get_including_interval(i, self.source_ranges)
        if interval:
            offset = i - interval[0]
            dest = self.get_corresponding_destination(interval)
            return dest[0] + offset
        else:
            return i

    def get_corresponding_destination(self, interval):
        return self.dest_ranges[self.source_ranges.index(interval)]

    def get_including_interval(self, i, intervals):
        for interval in intervals:
            if interval[0] <= i <= interval[1]:
                return interval
        return []

    @classmethod
    def from_starts_and_length(cls, dest_start, source_start, length):
        rm = cls([], [])
        rm.add_from_starts_and_length(dest_start, source_start, length)
        return rm

    @classmethod
    def from_starts_and_lengths_str(cls, str_repr):
        rm = cls([], [])
        for line in str_repr.strip().split('\n'):
            rm.add_from_starts_and_length(*map(int, line.strip().split()))
        return rm

    def __repr__(self):
        res = ""
        for s, d in zip(self.source_ranges, self.dest_ranges):
            res += f"{s} -> {d}\n"
        return res[:-1]

    def __getitem__(self, key):
        return self.find_correspondance(key)
