from typing import Dict, List

class Agent:
    def __init__(self, name: str, knowledge_graph: 'KnowledgeGraph'):
        self.name = name
        self.knowledge_graph = knowledge_graph

    def start(self) -> None:
        try:
            # Agent start logic
            pass
        except Exception as e:
            raise OrchestrationException(f"Agent {self.name} start failed: {e}")

    def stop(self) -> None:
        try:
            # Agent stop logic
            pass
        except Exception as e:
            raise OrchestrationException(f"Agent {self.name} stop failed: {e}")

class KnowledgeGraph:
    def __init__(self):
        self.state = {}

    def initialize(self) -> None:
        try:
            # Knowledge graph initialization logic
            pass
        except Exception as e:
            raise OrchestrationException(f"Knowledge graph initialization failed: {e}")

    def update(self, update: Dict) -> None:
        try:
            self.state.update(update)
        except Exception as e:
            raise OrchestrationException(f"Knowledge graph update failed: {e}")

    def get_state(self) -> Dict:
        try:
            return self.state.copy()  # Return a copy of the state to avoid modifying it
        except Exception as e:
            raise OrchestrationException(f"Knowledge graph get failed: {e}")

    def stop(self) -> None:
        try:
            # Knowledge graph stop logic
            pass
        except Exception as e:
            raise OrchestrationException(f"Knowledge graph stop failed: {e}")

    def __del__(self):
        self.stop()