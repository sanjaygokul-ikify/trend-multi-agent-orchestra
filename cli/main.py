import argparse
from packages.core import Agent, KnowledgeGraph, Engine
from services.orchestrator import Orchestrator

parser = argparse.ArgumentParser(description='Multi-Agent Orchestration Framework')
parser.add_argument('--agents', type=int, help='Number of agents', required=True)
parser.add_argument('--knowledge-graph', type=str, help='Knowledge graph configuration', required=True)

args = parser.parse_args()

agents = [Agent(f'Agent {i}', KnowledgeGraph()) for i in range(args.agents)]
engine = Engine(agents, KnowledgeGraph())
orchestrator = Orchestrator(engine)

orchestrator.start()