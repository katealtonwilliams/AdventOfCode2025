import math


class DayTwoSolver:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.parsed_input = None

    def parse_input(self):
        with open(self.input_file) as raw_ranges:
            self.parsed_input = [
                id_range.split("-") for id_range in raw_ranges.read().split(",")
            ]

    def calculate_invalid_ids_p1(self):
        self.parse_input()
        invalid_ids = 0
        for start, end in self.parsed_input:
            for possible_id in range(int(start), int(end) + 1):
                possible_id = str(possible_id)
                if (id_length := len(possible_id)) % 2 != 0:
                    continue
                first_half = possible_id[: int(id_length / 2)]
                second_half = possible_id[int(id_length / 2) :]
                if first_half == second_half:
                    invalid_ids += int(possible_id)
        return invalid_ids

    def find_largest_divisor(self, num) -> int | None:
        if num == 1:
            return None
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return num // i
        return 1

    def calculate_invalid_ids_p2(self):
        self.parse_input()
        invalid_ids = 0
        for start, end in self.parsed_input:
            for possible_id in range(int(start), int(end) + 1):
                possible_id = str(possible_id)
                id_length = len(possible_id)
                largest_divisor = self.find_largest_divisor(id_length)
                if not largest_divisor:
                    continue
                for pattern_length in range(1, largest_divisor + 1):
                    if id_length % pattern_length == 0:
                        pattern = possible_id[:pattern_length]
                        if pattern * (id_length // pattern_length) == possible_id:
                            invalid_ids += int(possible_id)
                            break
        return invalid_ids


if __name__ == "__main__":

    print("\n-------Answers-------\n")

    practise_solver = DayTwoSolver("day2/day2_example_input.txt")
    print(f"Part 1 practise: {practise_solver.calculate_invalid_ids_p1()}\n")

    final_solver = DayTwoSolver("day2/day2_input.txt")
    print(f"Part 1 real: {final_solver.calculate_invalid_ids_p1()}\n")

    practise_solver = DayTwoSolver("day2/day2_example_input.txt")
    print(f"Part 2 practise: {practise_solver.calculate_invalid_ids_p2()}\n")

    practise_solver = DayTwoSolver("day2/day2_input.txt")
    print(f"Part 2 real: {final_solver.calculate_invalid_ids_p2()}\n")
