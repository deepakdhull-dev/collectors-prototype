from .base import BaseCollector


class CPUCollector(BaseCollector):
    def __init__(self):
        self.prev_stats = None

    def _read_proc(self):
        with open("/proc/stat", "r") as f:
            x = f.readline()
            return [int(y) for y in x.split()[1:]]

    def collect(self):
        curr = self._read_proc()
        if self.prev_stats == None:
            self.prev_stats = curr
            return 0.0
        prev = self.prev_stats
        prev_idle = prev[3] + prev[4]
        curr_idle = curr[3] + curr[4]
        tot_prev = sum(prev)
        tot_curr = sum(curr)
        idle_delta = curr_idle - prev_idle
        tot_delta = tot_curr - tot_prev
        if tot_delta == 0:
            return 0.0
        self.prev_stats = curr
        return round((1 - idle_delta / tot_delta) * 100, 2)
