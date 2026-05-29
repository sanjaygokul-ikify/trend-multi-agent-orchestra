from typing import Dict, List

class Agent:
    def __init__(self, name: str, knowledge_graph: 'KnowledgeGraph'):
        self.name = name
        self.knowledge_graph = knowledge_graph

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

class KnowledgeGraph:
    def __init__(self):
        self.state = {}

    def initialize(self) -> None:
        pass

    def update(self, update: Dict) -> None:
        self.state.update(update)

    def get_state(self) -> Dict:
        return self.state

    def stop(self) -> None:
        pass

    def __del__(self):
        self.stop()