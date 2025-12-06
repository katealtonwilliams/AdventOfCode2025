import numpy as np


class DaySixSolver:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.calculations = None

    def parse_input_p1(self):
        with open(self.input_file) as raw_calculations:
            horizontal_calcs = [
                line.strip().split() for line in raw_calculations.readlines()
            ]
        correctly_oriented_calcs = []
        for idx in range(len(horizontal_calcs[0])):
            correctly_oriented_calcs.append([calc[idx] for calc in horizontal_calcs])
        self.calculations = correctly_oriented_calcs

    def is_blank_space(self, check: str) -> bool:
        return check == " "

    def parse_input_p2(self):
        with open(self.input_file) as raw_calcs:
            horizontal_calcs = np.array([[i for i in line][:-1] for line in raw_calcs])
        separate_calcs = []
        start_idx = 0
        for idx, line in enumerate(vertical_calcs := horizontal_calcs.T):
            if np.all(line == " "):
                new_calc = vertical_calcs[start_idx:idx].T
                separate_calcs.append(new_calc)
                start_idx = idx + 1
        final_calc = vertical_calcs[start_idx:].T
        separate_calcs.append(final_calc)
        self.calculations = separate_calcs

    def calculate_total_p1(self) -> int:
        self.parse_input_p1()
        total = 0
        for calculation in self.calculations:
            operator = calculation[-1]
            total += eval(operator.join(calculation[:-1]))
        return total

    def calculate_total_p2(self) -> int:
        self.parse_input_p2()
        total = 0
        for calculation in self.calculations:
            operator = calculation[-1, 0]
            calc = ""
            for number in calculation.T:
                calc += "".join(number[:-1])
                calc += operator
            total += eval(calc[:-1])

        return total


if __name__ == "__main__":

    print("\n-------Answers-------\n")

    practise_solver = DaySixSolver("day6/day6_example_input.txt")
    print(f"Part 1 practise: {practise_solver.calculate_total_p1()}\n")

    final_solver = DaySixSolver("day6/day6_input.txt")
    print(f"Part 1 real: {final_solver.calculate_total_p1()}\n")

    practise_solver = DaySixSolver("day6/day6_example_input.txt")
    print(f"Part 2 practise: {practise_solver.calculate_total_p2()}\n")

    practise_solver = DaySixSolver("day6/day6_input.txt")
    print(f"Part 2 real: {final_solver.calculate_total_p2()}\n")
