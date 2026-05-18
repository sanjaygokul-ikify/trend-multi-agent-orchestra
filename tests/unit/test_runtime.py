import unittest
from packages.core import Engine

class TestRuntime(unittest.TestCase):
    def test_engine_start_stop(self) -> None:
        agents = [Agent('Agent 1', KnowledgeGraph()), Agent('Agent 2', KnowledgeGraph())]
        engine = Engine(agents, KnowledgeGraph())
        engine.start()
        engine.stop()
        self.assertTrue(True)
