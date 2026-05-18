from packages.core import Engine

class Orchestrator:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine
    
    def start(self) -> None:
        self.engine.start()
    
    def stop(self) -> None:
        self.engine.stop()