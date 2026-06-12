import os

from .base import BaseCollector


class LoadCollector(BaseCollector):
    def collect(self):
        load = os.getloadavg()
        return {
            "load_1m": round(load[0], 2),
            "load_5m": round(load[1], 2),
            "load_15m": round(load[2], 2),
        }
