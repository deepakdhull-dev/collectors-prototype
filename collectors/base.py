class BaseCollector:
    def collect(self):
        raise NotImplementedError(f"{self.__class__.__name__} must implement collect")

    def collect_safe(self):
        try:
            return self.collect()
        except Exception as e:
            return {"error": e, "collector": self.__class__.__name__}
