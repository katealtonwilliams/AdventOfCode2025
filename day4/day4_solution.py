import numpy as np


class DayFourSolver:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.roll_diagram = None

    def parse_input(self):
        with open(self.input_file) as raw_diagram:
            diagram = [[i for i in line.strip()] for line in raw_diagram.readlines()]
        self.roll_diagram = np.array(diagram)

    def get_surrounding_one_axis(
        self, current_pos: int, max_pos: int
    ) -> tuple[bool, int]:
        valid_pos = []
        for pos_dif in range(-1, 2):
            new_pos = pos_dif + current_pos
            if new_pos >= 0 and new_pos < max_pos:
                valid_pos.append(new_pos)
        return valid_pos

    def get_surrounding_coords(
        self, current_row: int, current_column: int, max_row: int, max_col: int
    ) -> list[tuple]:
        adj_pos = []
        for valid_row in self.get_surrounding_one_axis(current_row, max_row):
            for valid_col in self.get_surrounding_one_axis(current_column, max_col):
                adj_pos.append((valid_row, valid_col))
        adj_pos.remove((current_row, current_column))
        return adj_pos

    def find_current_accessible_rolls(self) -> list[tuple[int, int]]:
        if self.roll_diagram is None:
            self.parse_input()
        max_row, max_col = self.roll_diagram.shape
        paper_row_idx, paper_col_idx = np.where(self.roll_diagram == "@")
        accessible_paper_roll_positions = []
        for row, col in zip(paper_row_idx, paper_col_idx):
            surrounding_paper_count = 0
            for adj_row, adj_col in self.get_surrounding_coords(
                row, col, max_row, max_col
            ):
                surrounding_paper_count += self.roll_diagram[adj_row, adj_col] == "@"
                if surrounding_paper_count > 3:
                    break
            if surrounding_paper_count < 4:
                accessible_paper_roll_positions.append((row, col))
        return accessible_paper_roll_positions

    def find_all_accessible_rolls(self) -> int:
        roll_count = 0
        while len(current_rolls := self.find_current_accessible_rolls()) > 0:
            roll_count += len(current_rolls)
            for roll_row, roll_col in current_rolls:
                self.roll_diagram[roll_row, roll_col] = "."
        return roll_count


if __name__ == "__main__":

    print("\n-------Answers-------\n")

    practise_solver = DayFourSolver("day4/day4_example_input.txt")
    print(f"Part 1 practise: {len(practise_solver.find_current_accessible_rolls())}\n")

    final_solver = DayFourSolver("day4/day4_input.txt")
    print(f"Part 1 real: {len(final_solver.find_current_accessible_rolls())}\n")

    practise_solver = DayFourSolver("day4/day4_example_input.txt")
    print(f"Part 2 practise: {practise_solver.find_all_accessible_rolls()}\n")

    final_solver = DayFourSolver("day4/day4_input.txt")
    print(f"Part 2 practise: {final_solver.find_all_accessible_rolls()}\n")
