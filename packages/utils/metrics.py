import time

class Metric:
    def __init__(self, name: str) -> None:
        self.name = name
        self.start_time = time.time()
    
    def get_elapsed_time(self) -> float:
        return time.time() - self.start_time