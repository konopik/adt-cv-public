# TODO 0 pipem nainstalovat
# https://github.com/JakubSido/adthelpers

# pip install git+https://github.com/JakubSido/adthelpers
# nebo stáhnout zip a instalovat jako pip install <cesta_k_rozbalenému_zipu>

import json
from queue import PriorityQueue
from tqdm import tqdm
import adthelpers

import plotly.express as px


class Graph:
    def __init__(self, directed: bool = False) -> None:
        self.edges: dict[int, list[tuple[float, int]]] = {}
        self.oriented = directed
        self.edge_count = 0

    def add_edge(self, src: int, dst: int, weight: float = 0) -> None:
        
        if src not in self.edges:
            self.edges[src] = []
        self.edges[src].append((weight, dst))
        if dst not in self.edges:
            self.edges[dst] = []
        self.edges[dst].append((weight, src))

    def dijkstra(
        self, start_id: int, end_id: int, show_progress: bool = True,
    ) -> tuple[dict[int, float], dict[int, int]]:
        closed: set[int] = set()
        sp_tree: list[tuple[int, int]] = []
        queue: PriorityQueue = PriorityQueue()

        # navíc
        distances: dict[int, float] = {}
        predecessors: dict[int, int] = {}

        if show_progress:
            painter = adthelpers.painter.Painter(
                self,
                visible=queue,
                closed=closed,
                color_edges=sp_tree,
                distances=distances,  # navic
            )
            painter.draw_graph()
        else:
            painter = None

        # TODO 1 Implementujte Dijkstrův algoritmus pro nalezení nejkratší cesty
        from dataclasses import dataclass, field
        @dataclass(order=True)
        class PriorityEdge:
            priority:int
            edge:tuple[int,int] = field(compare=False)
            def __getitem__(self, key):
                if key > 1:
                    raise IndexError
                return self.edge if key == 1 else self.priority
        distances[start_id] = 0
        queue.put(PriorityEdge(0,(-1,start_id)))
        while not queue.empty():
            current_priority,(start,dist) = queue.get()
            if dist not in closed:
                closed.add(dist)
                if painter:
                    painter.draw_graph(active=dist)
                if start != dist:
                    predecessors[dist] = start
                    sp_tree.append((start,dist))

                if dist == end_id:
                    break
                for weight, neightbor in self.edges[dist]:
                    if neightbor in closed:
                        continue
                    new_distance = distances[dist] + weight

                    if neightbor not in distances or new_distance < distances[neightbor]:
                        distances[neightbor] = new_distance
                        queue.put(PriorityEdge(new_distance,(dist,neightbor)))



        return distances, predecessors


def load_graph(filename: str) -> Graph:
    graph = Graph(directed=False)

    with open(filename, encoding="utf-8") as f:
        data = json.load(f)

    for edge in data["links"]:
        node1, node2 = edge["source"], edge["target"]
        graph.add_edge(node1, node2, edge["weight"])

    return graph


def load_graph_csv(filename: str) -> Graph:
    graph = Graph(directed=True)
    with open(filename,'r',encoding='utf8') as f:
        next(f)
        for line in f:
            data = line.split(',')
            start = int(data[0])
            target = int(data[1])
            weight = float(data[2])
            if start in graph.edges:
                graph.edges[start].append((weight,target))
            else:
                graph.edges[start] = []
                graph.edges[start].append((weight,target))


    # TODO 3 Načtěte graf z CSV souboru

    return graph


def reconstruct_path(
    predecessors: dict[int, int], start_id: int, end_id: int,
) -> list[int]:
    path = []
    ## TODO 2 Implementujte funkci pro rekonstrukci cesty podle předchůdců
    current = end_id
    while current is not None:
        path.append(current)
        if current == start_id:
            break
        current = predecessors.get(current)
    path.reverse()
    return path



def load_nodes_metadata(filename: str) -> dict[int, tuple[str, str]]:
    """Načte metadata o uzlech z CSV souboru. V případě GPS dat je možné zobrazit trasu na mapě
    pomocí plotly express.
    Returns:
        dict[int, tuple[str, str]]: metadata uzlů (id uzlu, [latitude, longitude])
    """
    node_info = {}
    ## TODO 4 Načtěte metadata o uzlech z CSV souboru
    
    return node_info


def show_path(
    node_info: dict[int, tuple[str, str]],  # metadata uzlů načtená pomocí load_nodes_metadata
    path: list[int],
) -> None:
    """
    Args:
        node_info (dict[int, tuple[str, str]]): metadata uzlů načtená pomocí load_nodes_metadata
        path (list[int]): cesta získaná pomocí reconstruct_path
    """
    if node_info:
        lats = [float(la) for la, lo in [node_info[p] for p in path]]
        lons = [float(lo) for la, lo in [node_info[p] for p in path]]

        fig = px.line_mapbox(lat=lats, lon=lons, mapbox_style="open-street-map", zoom=12)
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, mapbox_center_lat=49.747)
        fig.show()


def demo() -> None:
    graph = load_graph("10-spanning-tree/data/graph_grid_s3_3.json")

    # painter = adthelpers.painter.Painter(
    #     graph,
    #     #colors=("red", "blue", "yellow", "grey") # pokud by byl problém s barvami je možné změnit
    # )
    # painter.draw_graph()
    start = 0
    end = 8
    distances, predecessors = graph.dijkstra(start, end)
    path = reconstruct_path(predecessors, start, end)
    print(path)
    print(distances[end])


def pilsen() -> None:
    edge_file = "11-12-dijkstra/pilsen/pilsen_edges_nice.csv"
    node_file = "11-12-dijkstra/pilsen/pilsen_nodes.csv"
    graph = load_graph_csv(edge_file)
    start = 4651
    end = 4569
    distances, predecessors = graph.dijkstra(start, end, show_progress=False)
    path = reconstruct_path(predecessors, start, end)
    show_path(
        load_nodes_metadata(node_file),
        path,
    )
    print(path)
    print(distances[end])


def main() -> None:
    #demo()
    pilsen()
    input("...")


if __name__ == "__main__":
    main()
