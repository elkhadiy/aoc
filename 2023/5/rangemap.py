from bisect import bisect


class RangeMap:

    def __init__(self, str_repr):
        self.source_ranges = []
        self.dest_ranges = []
        self.ranges = list(zip(self.source_ranges, self.dest_ranges))
        for line in str_repr.strip().split('\n'):
            dest, source, length = [int(val) for val in line.strip().split()]
            self.add_from_starts_and_length(dest, source, length)

    def add_range(self, dest, source):
        lo = bisect([x[0][0] for x in self.ranges], source[0])
        self.ranges.insert(lo, (source, dest))
        self.source_ranges = [r[0] for r in self.ranges]
        self.dest_ranges = [r[1] for r in self.ranges]
        self.source_range_key = [r[0] for r in self.source_ranges]

    def add_from_starts_and_length(self, dest_start, source_start, length):
        self.add_range((dest_start, dest_start + length - 1),
                       (source_start, source_start + length - 1))

    def find_correspondance(self, i):
        interval = self.get_including_interval(i)
        if interval:
            offset = i - interval[0]
            dest = self.get_corresponding_destination(interval)
            return dest[0] + offset
        else:
            return i

    def get_corresponding_destination(self, interval):
        return self.dest_ranges[self.source_ranges.index(interval)]

    def get_including_interval_brute(self, i, intervals):
        for interval in intervals:
            if interval[0] <= i <= interval[1]:
                return interval
        return []

    def get_including_interval(self, i):
        lo = bisect(self.source_range_key, i)
        if 0 < lo <= len(self.source_range_key) and i <= self.source_ranges[lo-1][1]:
            return self.source_ranges[lo-1]
        return []

    def __repr__(self):
        res = ""
        for s, d in zip(self.source_ranges, self.dest_ranges):
            res += f"{s} -> {d}\n"
        return res[:-1]

    def __getitem__(self, key):
        return self.find_correspondance(key)
