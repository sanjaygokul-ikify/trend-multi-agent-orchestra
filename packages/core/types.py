from typing import Dict, List

class Agent:
    def __init__(self, name: str, knowledge_graph: 'KnowledgeGraph'):
        self.name = name
        self.knowledge_graph = knowledge_graph

    def start(self):
        pass

    def stop(self):
        pass

class KnowledgeGraph:
    def __init__(self):
        self.state = {}

    def initialize(self):
        pass

    def update(self, update: Dict):
        self.state.update(update)

    def get_state(self):
        return self.state

    def stop(self):
        pass
