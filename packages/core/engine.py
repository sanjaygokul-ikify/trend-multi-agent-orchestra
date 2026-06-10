import logging
from typing import List, Dict
from .types import Agent, KnowledgeGraph
from .exceptions import OrchestrationException

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self, agents: List[Agent], knowledge_graph: KnowledgeGraph):
        self.agents = agents
        self.knowledge_graph = knowledge_graph
        self.coordination_layer = None
        self.plugin_bus = None
        self.execution_engine = None

    def start(self):
        try:
            # Initialize coordination layer
            self.coordination_layer = CoordinationLayer(self.agents, self.knowledge_graph)
            # Initialize plugin bus
            self.plugin_bus = PluginBus(self.agents, self.knowledge_graph)
            # Initialize execution engine
            self.execution_engine = ExecutionEngine(self.agents, self.knowledge_graph)
            # Start agents
            for agent in self.agents:
                try:
                    agent.start()
                except Exception as e:
                    logger.error(f"Agent {agent.name} start failed: {e}")
                    raise OrchestrationException(f"Agent {agent.name} start failed: {e}")
            # Initialize knowledge graph
            self.knowledge_graph.initialize()
            # Start coordination layer
            self.coordination_layer.start()
            # Start plugin bus
            self.plugin_bus.start()
            # Start execution engine
            self.execution_engine.start()
        except Exception as e:
            logger.error(f"Engine start failed: {e}")
            raise OrchestrationException(f"Engine start failed: {e}")

    def stop(self):
        try:
            # Stop execution engine
            if self.execution_engine:
                self.execution_engine.stop()
            # Stop plugin bus
            if self.plugin_bus:
                self.plugin_bus.stop()
            # Stop coordination layer
            if self.coordination_layer:
                self.coordination_layer.stop()
            # Stop agents
            for agent in self.agents:
                try:
                    agent.stop()
                except Exception as e:
                    logger.error(f"Agent {agent.name} stop failed: {e}")
                    raise OrchestrationException(f"Agent {agent.name} stop failed: {e}")
            # Stop knowledge graph
            self.knowledge_graph.stop()
        except Exception as e:
            logger.error(f"Engine stop failed: {e}")
            raise OrchestrationException(f"Engine stop failed: {e}")

    def update_knowledge_graph(self, update: Dict):
        try:
            self.knowledge_graph.update(update)
        except Exception as e:
            logger.error(f"Knowledge graph update failed: {e}")
            raise OrchestrationException(f"Knowledge graph update failed: {e}")

    def get_knowledge_graph(self):
        try:
            return self.knowledge_graph.get_state()
        except Exception as e:
            logger.error(f"Knowledge graph get failed: {e}")
            raise OrchestrationException(f"Knowledge graph get failed: {e}")

    def __del__(self):
        self.stop()

    def __repr__(self) -> str:
        return f"Engine({self.agents}, {self.knowledge_graph})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Engine):
            return False
        return self.agents == other.agents and self.knowledge_graph == other.knowledge_graph

class CoordinationLayer:
    def __init__(self, agents: List[Agent], knowledge_graph: KnowledgeGraph):
        self.agents = agents
        self.knowledge_graph = knowledge_graph
        self.plugin_bus = None
        self.execution_engine = None
        self._stop = False

    def start(self):
        try:
            # Initialize plugin bus
            self.plugin_bus = PluginBus(self.agents, self.knowledge_graph)
            # Initialize execution engine
            self.execution_engine = ExecutionEngine(self.agents, self.knowledge_graph)
            # Start plugin bus
            self.plugin_bus.start()
            # Start execution engine
            self.execution_engine.start()
            # Create a new thread for the coordination layer
            import threading
            threading.Thread(target=self._run).start()
        except Exception as e:
            logger.error(f"Coordination layer start failed: {e}")
            raise OrchestrationException(f"Coordination layer start failed: {e}")

    def _run(self):
        while not self._stop:
            # Perform the actual coordination
            try:
                self.knowledge_graph.update({"coordination_layer": "running"})
            except Exception as e:
            # Add a try/except block to handle the exception
                try:
                    logger.error(f"Coordination layer update failed: {e}")
                    raise OrchestrationException(f"Coordination layer update failed: {e}")
                except Exception as ex:
                    logger.error(f"Coordination layer exception: {ex}")
            # Introduce a small delay to simulate the coordination time
            import time
            time.sleep(0.1)

    def stop(self):
        try:
            # Stop execution engine
            if self.execution_engine:
                self.execution_engine.stop()
            # Stop plugin bus
            if self.plugin_bus:
                self.plugin_bus.stop()
            self._stop = True
        except Exception as e:
            logger.error(f"Coordination layer stop failed: {e}")
            raise OrchestrationException(f"Coordination layer stop failed: {e}")

    def update(self, update: Dict):
        try:
            self.knowledge_graph.update(update)
        except Exception as e:
            logger.error(f"Coordination layer update failed: {e}")
            raise OrchestrationException(f"Coordination layer update failed: {e}")

    def get_state(self):
        try:
            return self.knowledge_graph.get_state()
        except Exception as e:
            logger.error(f"Coordination layer get failed: {e}")
            raise OrchestrationException(f"Coordination layer get failed: {e}")

    def __del__(self):
        self.stop()

    def __repr__(self) -> str:
        return f"CoordinationLayer({self.agents}, {self.knowledge_graph})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CoordinationLayer):
            return False
        return self.agents == other.agents and self.knowledge_graph == other.knowledge_graph

class PluginBus:
    def __init__(self, agents: List[Agent], knowledge_graph: KnowledgeGraph):
        self.agents = agents
        self.knowledge_graph = knowledge_graph
        self.plugins = {}

    def start(self):
        try:
            # Initialize plugins
            for plugin in self.plugins:
                self.plugins[plugin].start()
        except Exception as e:
            logger.error(f"Plugin bus start failed: {e}")
            raise OrchestrationException(f"Plugin bus start failed: {e}")

    def stop(self):
        try:
            # Stop plugins
            for plugin in self.plugins:
                self.plugins[plugin].stop()
        except Exception as e:
            logger.error(f"Plugin bus stop failed: {e}")
            raise OrchestrationException(f"Plugin bus stop failed: {e}")

    def add_plugin(self, plugin):
        try:
            self.plugins[plugin.name] = plugin
        except Exception as e:
            logger.error(f"Plugin bus add failed: {e}")
            raise OrchestrationException(f"Plugin bus add failed: {e}")

    def remove_plugin(self, plugin_name):
        try:
            if plugin_name in self.plugins:
                del self.plugins[plugin_name]
            else:
                raise OrchestrationException(f"Plugin {plugin_name} not found")
        except Exception as e:
            logger.error(f"Plugin bus remove failed: {e}")
            raise OrchestrationException(f"Plugin bus remove failed: {e}")

    def __del__(self):
        self.stop()

    def __repr__(self) -> str:
        return f"PluginBus({self.agents}, {self.knowledge_graph})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PluginBus):
            return False
        return self.agents == other.agents and self.knowledge_graph == other.knowledge_graph

class ExecutionEngine:
    def __init__(self, agents: List[Agent], knowledge_graph: KnowledgeGraph):
        self.agents = agents
        self.knowledge_graph = knowledge_graph
        self.tasks = {}

    def start(self):
        try:
            # Initialize tasks
            for task in self.tasks:
                self.tasks[task].start()
        except Exception as e:
            logger.error(f"Execution engine start failed: {e}")
            raise OrchestrationException(f"Execution engine start failed: {e}")

    def stop(self):
        try:
            # Stop tasks
            for task in self.tasks:
                self.tasks[task].stop()
        except Exception as e:
            logger.error(f"Execution engine stop failed: {e}")
            raise OrchestrationException(f"Execution engine stop failed: {e}")

    def add_task(self, task):
        try:
            self.tasks[task.name] = task
        except Exception as e:
            logger.error(f"Execution engine add failed: {e}")
            raise OrchestrationException(f"Execution engine add failed: {e}")

    def remove_task(self, task_name):
        try:
            if task_name in self.tasks:
                del self.tasks[task_name]
            else:
                raise OrchestrationException(f"Task {task_name} not found")
        except Exception as e:
            logger.error(f"Execution engine remove failed: {e}")
            raise OrchestrationException(f"Execution engine remove failed: {e}")

    def __del__(self):
        self.stop()

    def __repr__(self) -> str:
        return f"ExecutionEngine({self.agents}, {self.knowledge_graph})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ExecutionEngine):
            return False
        return self.agents == other.agents and self.knowledge_graph == other.knowledge_graph
