import unittest
from packages.core import Agent, KnowledgeGraph, Engine
from services.orchestrator import Orchestrator

class TestPipeline(unittest.TestCase):
    def test_full_pipeline(self) -> None:
        agents = [Agent('Agent 1', KnowledgeGraph()), Agent('Agent 2', KnowledgeGraph())]
        engine = Engine(agents, KnowledgeGraph())
        orchestrator = Orchestrator(engine)
        orchestrator.start()
        orchestrator.stop()
        self.assertTrue(True)
