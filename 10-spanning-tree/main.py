# TODO 0 pipem nainstalovat
# https://github.com/JakubSido/adthelpers

# pip install git+https://github.com/JakubSido/adthelpers
# nebo stáhnout zip a instalovat jako pip install <cesta_k_rozbalenému_zipu>

from collections import defaultdict
import json
from queue import PriorityQueue
from dataclasses import dataclass,field
import adthelpers


class Graph:
    def __init__(self) -> None:
        self.edges: dict[int, list[tuple[float, int]]] = defaultdict(list)

    def add_edge(self, src: int, dst: int, weight: float = 0) -> None:
        # TODO 1 napište kód přidání hrany do datové struktury grafu

        self.edges[src].append((weight,dst))
        self.edges[dst].append((weight,src))
        


def load_graph(filename: str) -> Graph:
    graph = Graph()

    # TODO 2 vytvořte graf podle dat ze souboru
    with open(filename,"r") as f:
        graph_data=json.load(f)
    for edge in graph_data["links"]:
        graph.add_edge(edge["source"],edge["target"],edge["weight"])
    return graph
    


def spanning_tree(graph: Graph) -> None:
    closed: set[int] = set()
    sp_tree: list[tuple[int, int]] = []
    queue: PriorityQueue = PriorityQueue()

    painter = adthelpers.painter.Painter(
        graph,
        visible=queue,
        closed=closed,
        color_edges=sp_tree,
    )
    painter.draw_graph()
    @dataclass(order=True)
    class PriorityEdge:
        priority : int
        edge : tuple[int, int] = field(compare=False)

        def getitem(self, key):
            if key > 1:
                raise IndexError("PriorityEdge only has two fields: edge and priority")
            return self.edge if key == 1 else self.priority
    # TODO 3 Implementujte Prim-Jarníkův algoritmus pro nalezení minimální kostry
    queue.put((0,(0,0)))
    while not queue.empty():
        current_edge=queue.get()
        dst=current_edge[1][1]
        if dst in closed:
            continue
        closed.add(dst)
        sp_tree.append(current_edge.edge)
        for edge in graph.edges[dst]:
            if edge[1]not in closed:
                queue.put((int(edge[0]),(dst,edge[1])))
        painter.draw_graph(dst)

def main() -> None:
    graph = load_graph("10-spanning-tree/data/graph_grid_s3_3.json")

    painter = adthelpers.painter.Painter(
        graph,
        # colors=("red", "blue", "yellow", "grey") # pokud by byl problém s barvami je možné změnit
    )
    painter.draw_graph()

    # debug to see progress...
    spanning_tree(graph)

    # don't close before user acknowledges diagrams
    input("Press enter to exit program...")

if __name__ == "__main__":
    main()
