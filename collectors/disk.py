import shutil

from .base import BaseCollector


class DiskCollector(BaseCollector):
    def __init__(self, path: str = "/"):
        super().__init__()
        self.path = path

    def collect(self):
        usage = shutil.disk_usage(self.path)
        total_gb = round(usage.total / 1024**3, 1)
        used_gb = round(usage.used / 1024**3, 1)
        free_gb = round(usage.free / 1024**3, 1)
        return {
            "total_disk_gb": total_gb,
            "used_disk_gb": used_gb,
            "free_disk_gb": free_gb,
            "disk_percent_used_gb": round(used_gb / total_gb, 2),
            "path": self.path,
        }
