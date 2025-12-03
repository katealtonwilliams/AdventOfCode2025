from copy import deepcopy


class DayThreeSolver:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.parsed_input = None

    def parse_input(self):
        with open(self.input_file) as raw_banks:
            self.parsed_input = [
                [int(i) for i in bank.strip()] for bank in raw_banks.readlines()
            ]

    def calculate_joltage_p1(self) -> int:
        self.parse_input()
        joltage = 0
        for bank in self.parsed_input:
            start_number = max(bank[:-1])
            start_number_index = bank.index(start_number)
            end_number = max(bank[start_number_index + 1 :])
            joltage += int(str(start_number) + str(end_number))
        return joltage

    def calculate_joltage(self, num_batteries: int) -> int:
        self.parse_input()
        total_joltage = 0
        for bank in self.parsed_input:
            batteries_remaining = deepcopy(num_batteries)
            joltage = ""
            while batteries_remaining > 1:
                next_number = max(bank[: -(batteries_remaining - 1)])
                current_index = bank.index(next_number)
                bank = bank[current_index + 1 :]
                joltage += str(next_number)
                batteries_remaining -= 1
            final_number = max(bank)
            joltage += str(final_number)
            total_joltage += int(joltage)
        return total_joltage


if __name__ == "__main__":

    print("\n-------Answers-------\n")

    practise_solver = DayThreeSolver("day3/day3_example_input.txt")
    print(f"Part 1 practise: {practise_solver.calculate_joltage(2)}\n")

    final_solver = DayThreeSolver("day3/day3_input.txt")
    print(f"Part 1 real: {final_solver.calculate_joltage(2)}\n")

    practise_solver = DayThreeSolver("day3/day3_example_input.txt")
    print(f"Part 2 practise: {practise_solver.calculate_joltage(12)}\n")

    practise_solver = DayThreeSolver("day3/day3_input.txt")
    print(f"Part 2 real: {practise_solver.calculate_joltage(12)}\n")
