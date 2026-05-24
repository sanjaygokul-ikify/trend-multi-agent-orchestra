import logging
from typing import Dict
from packages.core.engine import Engine
logger = logging.getLogger(__name__)

class Executor:
    def __init__(self):
        self.engine = None

    def start(self, agents: List['Agent'], knowledge_graph: 'KnowledgeGraph'):
        self.engine = Engine(agents, knowledge_graph)
        self.engine.start()

    def stop(self):
        if self.engine:
            self.engine.stop()

    def update_knowledge_graph(self, update: Dict):
        if self.engine:
            self.engine.update_knowledge_graph(update)

    def get_knowledge_graph(self):
        if self.engine:
            return self.engine.get_knowledge_graph()