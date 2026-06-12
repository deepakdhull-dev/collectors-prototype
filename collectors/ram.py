from .base import BaseCollector


class RamCollector(BaseCollector):
    def collect(self):
        mem = dict()
        with open("/proc/meminfo") as f:
            rd = f.readlines()
            for line in rd:
                parts = line.split(":")
                key = parts[0].strip()
                value = int(parts[1].strip().split()[0])
                mem[key] = value
        tot_mem = mem["MemTotal"] // 1024
        ava_mem = mem["MemAvailable"] // 1024
        used_mem = tot_mem - ava_mem
        col = 8
        return {
            "total_mem": tot_mem,
            "used_mem": used_mem,
            "ava_mem": ava_mem,
            "percent_mem": round(used_mem / tot_mem * 100, 2),
        }
