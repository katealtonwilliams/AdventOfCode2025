class DayOneSolver:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.parsed_input = None

    def parse_input(self) -> dict[str:int]:
        with open(self.input_file) as raw_directions:
            self.parsed_input = [
                (line.strip()[0], int(line.strip()[1:]))
                for line in raw_directions.readlines()
            ]

    def rotate(self, current_point: int, direction: str, distance: int) -> int:
        if direction == "L":
            return current_point - distance
        elif direction == "R":
            return current_point + distance

    def calculate_answer_p1(self, start_point: int = 50) -> int:
        self.parse_input()
        reached_zero_count = 0
        current_point = start_point
        for direction, distance in self.parsed_input:
            current_point = self.rotate(current_point, direction, distance)
            if (current_point := current_point % 100) == 0:
                reached_zero_count += 1
        return reached_zero_count

    def calculate_answer_p2(self, start_point: int = 50) -> int:
        self.parse_input()
        reached_zero_count = 0
        current_point = start_point
        for direction, distance in self.parsed_input:
            new_point = self.rotate(current_point, direction, distance)
            if new_point * current_point < 0 or new_point == 0:
                reached_zero_count += 1
            reached_zero_count += abs(new_point) // 100
            current_point = new_point % 100
        return reached_zero_count


if __name__ == "__main__":

    print("\n-------Answers-------\n")

    practise_solver = DayOneSolver("day1/day1_example_input.txt")
    print(f"Part 1 Practise: {practise_solver.calculate_answer_p1()}\n")

    final_solver = DayOneSolver("day1/day1_input.txt")
    print(f"Part 1 real: {final_solver.calculate_answer_p1()}\n")

    practise_solver = DayOneSolver("day1/day1_example_input.txt")
    print(f"Part 2 practise: {practise_solver.calculate_answer_p2()}\n")

    final_solver = DayOneSolver("day1/day1_input.txt")
    print(f"Part 2 real: {final_solver.calculate_answer_p2()}\n")
