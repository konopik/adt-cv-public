# TODO 0 pipem nainstalovat
# https://github.com/JakubSido/adthelpers

# pip install git+https://github.com/JakubSido/adthelpers
# nebo stáhnout zip a instalovat jako pip install <cesta_k_rozbalenému_zipu>


import json
from queue import PriorityQueue
from collections import defaultdict
import adthelpers


class Graph:
    def __init__(self) -> None:
        self.edges: dict[int, list[tuple[float, int]]] = defaultdict(list)

    def add_edge(self, src: int, dst: int, weight: float = 0.0) -> None:
        # TODO 1 napište kód přidání hrany do datové struktury grafu
        self.edges[src].append((weight,dst))
        self.edges[dst].append((weight,src))


def load_graph(filename: str) -> Graph:
    graph = Graph()
    with open(filename,'r') as f:
        d = json.load(f)
        for link in d['links']:
            src = link['source']
            dst = link['target']
            w = link['weight']
            graph.add_edge(src,dst,w)



    # TODO 2 vytvořte graf podle dat ze souboru
    with open(filename,'r') as f:
        data = json.load(f)
        for line in data['links']:
            src = line['source']
            dst = line['target']
            w = line['weight']
            graph.add_edge(src,dst,w)
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
    

    # TODO 3 Implementujte Prim-Jarníkův algoritmus pro nalezení minimální kostry
    from dataclasses import dataclass, field
    @dataclass(order=True)
    class PriorityEdge:
        priority:int
        edge:tuple[int,int] = field(compare=False)
        def __getitem__(self, key):
            if key > 1:
                raise IndexError
            return self.edge if key == 1 else self.priority
    
    for wiegh,dst in graph.edges[0]:
        edge = PriorityEdge(wiegh,(0,dst))
        queue.put(edge)
    
    while not queue.empty():
        current_edge = queue.get()
        dst = current_edge.edge[1]
        if dst not in closed:
            closed.add(dst)
            sp_tree.append(current_edge.edge)

            for weight,dist in graph.edges[dst]:
                if dist not in closed:
                    new_edge = PriorityEdge(weight,(dst,dist))
                    queue.put(new_edge)
    
    painter.draw_graph()




def main() -> None:
    graph = load_graph('10-spanning-tree\data\graph_grid_s3_3.json')

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
