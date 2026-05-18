import unittest
from packages.core import Agent, KnowledgeGraph, Engine

class TestCore(unittest.TestCase):
    def test_agent_creation(self) -> None:
        agent = Agent('Test Agent', KnowledgeGraph())
        self.assertEqual(agent.name, 'Test Agent')
    
    def test_engine_creation(self) -> None:
        agents = [Agent('Agent 1', KnowledgeGraph()), Agent('Agent 2', KnowledgeGraph())]
        engine = Engine(agents, KnowledgeGraph())
        self.assertEqual(len(engine.agents), 2)
