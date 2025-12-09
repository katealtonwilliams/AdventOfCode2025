import numpy as np
from collections import deque


class DaySevenSolver:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.grid_diagram = None
        self.split_count = 0
        self.edge_map = {}
        self.edge_list = []
        self.indegree_map = {}
        self.topo_order = []
        self.ways = None
        self.source = None

    def _parse_input(self):
        with open(self.input_file) as raw_diagram:
            grid_diagram = [[*line.strip()] for line in raw_diagram.readlines()]
        self.grid_diagram = np.array(grid_diagram)

    def _split_beams(self, current_row_idx: int):
        beam_row = self.grid_diagram[current_row_idx]
        splitter_row = self.grid_diagram[current_row_idx + 1]
        new_beam_row_idx = current_row_idx + 2
        new_beam_row = self.grid_diagram[new_beam_row_idx]
        beam_idxes = np.where(beam_row == "|")[0]
        for idx in beam_idxes:
            if splitter_row[idx] == "^":
                new_beam_row[idx - 1] = "|"
                new_beam_row[idx + 1] = "|"
                self.edge_map[(current_row_idx, idx)] = [
                    (new_beam_row_idx, idx - 1),
                    (new_beam_row_idx, idx + 1),
                ]
                self.split_count += 1
            else:
                new_beam_row[idx] = "|"
                self.edge_map[(current_row_idx, idx)] = [(new_beam_row_idx, idx)]

    def calculate_splits(self) -> int:
        self._parse_input()
        start_pos = np.where(self.grid_diagram[0] == "S")[0][0]
        self.grid_diagram[1, start_pos] = "|"
        self.source = (1, start_pos)
        for row_idx in range(1, len(self.grid_diagram) - 2):
            self._split_beams(row_idx)
        return self.split_count

    def _find_edge_list_and_indegree(self):
        self.indegree_map = {node: 0 for node in self.edge_map.keys()}
        all_end_edges = {edge for edges in self.edge_map.values() for edge in edges}
        for edge in all_end_edges:
            if edge not in self.edge_map.keys():
                self.edge_map[edge] = []
        for start_edge, end_edges in self.edge_map.items():
            for end_edge in end_edges:
                self.edge_list.append((start_edge, end_edge))
                self.indegree_map[end_edge] = self.indegree_map.get(end_edge, 0) + 1

    def _perform_topo_search(self):
        remaining_edges = deque()
        for node, indegree in self.indegree_map.items():
            if indegree == 0:
                remaining_edges.append(node)

        while remaining_edges:
            node = remaining_edges.popleft()
            self.topo_order.append(node)

            for neighbour in self.edge_map[node]:
                self.indegree_map[neighbour] -= 1
                if self.indegree_map[neighbour] == 0:
                    remaining_edges.append(neighbour)

    def _find_all_ways_to_each_node(self):
        self.ways = {node: 0 for node in self.edge_map.keys()}
        self.ways[self.source] = 1
        for node in self.topo_order:
            for neighbour in self.edge_map[node]:
                self.ways[neighbour] += self.ways[node]

    def calculate_total_paths(self):
        self.calculate_splits()
        self._find_edge_list_and_indegree()
        self._perform_topo_search()
        self._find_all_ways_to_each_node()
        total_paths = 0
        for node, ways in self.ways.items():
            if node[0] == len(self.grid_diagram) - 1:
                total_paths += ways
        return total_paths


if __name__ == "__main__":

    print("\n-------Answers-------\n")

    practise_solver = DaySevenSolver("day7/day7_example_input.txt")
    print(f"Part 1 practise: {practise_solver.calculate_splits()}\n")

    final_solver = DaySevenSolver("day7/day7_input.txt")
    print(f"Part 1 real: {final_solver.calculate_splits()}\n")

    practise_solver = DaySevenSolver("day7/day7_example_input.txt")
    print(f"Part 2 practise: {practise_solver.calculate_total_paths()}\n")

    final_solver = DaySevenSolver("day7/day7_input.txt")
    print(f"Part 2 real: {final_solver.calculate_total_paths()}\n")
