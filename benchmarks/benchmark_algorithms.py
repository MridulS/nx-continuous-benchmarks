"""Benchmarks for a certain set of algorithms"""

import networkx as nx
from networkx.algorithms import community
from benchmarks.utils import fetch_drug_interaction_network


class AlgorithmBenchmarks:
    timeout = 120
    nodes = 100
    params = [
        nx.erdos_renyi_graph(nodes, 0.05),
        nx.erdos_renyi_graph(nodes, 0.8),
        fetch_drug_interaction_network(),
    ]
    param_names = ["graph_type"]

    def time_betweenness_centrality(self, graph_type):
        _ = nx.betweenness_centrality(graph_type)

    def time_greedy_modularity_communities(self, graph_type):
        _ = community.greedy_modularity_communities(graph_type)

    def time_connected_components(self, graph_type):
        _ = list(nx.connected_components(graph_type))

    def time_average_clustering(self, graph_type):
        _ = nx.average_clustering(graph_type)
