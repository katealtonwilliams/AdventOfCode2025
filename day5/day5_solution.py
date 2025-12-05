class DayFiveSolver:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.ingredients = None
        self.ingredient_ranges = None

    def parse_input(self):
        with open(self.input_file) as raw_ingredients:
            all_lines = [line.strip() for line in raw_ingredients.readlines()]
        break_index = all_lines.index("")
        ingredient_ranges = [
            list(map(int, ingredient_range.split("-")))
            for ingredient_range in all_lines[:break_index]
        ]
        ingredients = [int(ingredient) for ingredient in all_lines[break_index + 1 :]]
        self.ingredient_ranges = ingredient_ranges
        self.ingredients = ingredients

    def calculate_fresh_ingredients_p1(self) -> int:
        self.parse_input()
        fresh_ingredient_count = 0
        for ingredient in self.ingredients:
            for lower_value, upper_value in self.ingredient_ranges:
                if ingredient >= lower_value and ingredient <= upper_value:
                    fresh_ingredient_count += 1
                    break
        return fresh_ingredient_count

    def is_completely_overlapping(
        self,
        lower_check_value: int,
        upper_check_value: int,
        current_ranges: list[tuple[int]],
    ) -> bool:
        for lower_value, upper_value in current_ranges:
            if lower_check_value >= lower_value and upper_check_value <= upper_value:
                return True
        return False

    def is_no_overlap(
        self,
        lower_check_value: int,
        upper_check_value: int,
        current_ranges: list[tuple[int]],
    ) -> bool:
        for lower_value, upper_value in current_ranges:
            if lower_check_value <= upper_value and upper_check_value >= lower_value:
                return False
        return True

    def is_no_overlap_single(
        self,
        lower_check_value: int,
        upper_check_value: int,
        lower_value: int,
        upper_value: int,
    ) -> bool:
        if lower_check_value <= upper_value and upper_check_value >= lower_value:
            return False
        return True

    def update_distinct_ranges(
        self,
        lower_check_value: int,
        upper_check_value: int,
        distinct_ranges: list[tuple[int]],
    ) -> list[tuple[int, int]]:
        for idx, (lower_value, upper_value) in enumerate(distinct_ranges):
            if not self.is_no_overlap_single(
                lower_check_value, upper_check_value, lower_value, upper_value
            ):
                new_lower_value = lower_value
                new_upper_value = upper_value
                if lower_check_value < lower_value:
                    new_lower_value = lower_check_value
                if upper_check_value > upper_value:
                    new_upper_value = upper_check_value
                distinct_ranges[idx] = (new_lower_value, new_upper_value)
        return distinct_ranges

    def refine_distinct_ranges(
        self, unrefined_ranges: list[tuple[int, int]]
    ) -> list[tuple[int, int]]:
        distinct_ranges = []
        for lower_value, upper_value in unrefined_ranges:
            if self.is_completely_overlapping(
                lower_value, upper_value, distinct_ranges
            ):
                continue
            if self.is_no_overlap(lower_value, upper_value, distinct_ranges):
                distinct_ranges.append((lower_value, upper_value))
                continue
            distinct_ranges = self.update_distinct_ranges(
                lower_value, upper_value, distinct_ranges
            )
        return distinct_ranges

    def calculate_fresh_ingredients_p2(self) -> int:
        self.parse_input()
        previous = self.ingredient_ranges
        while True:
            refined = self.refine_distinct_ranges(previous)
            if len(refined) == len(previous):
                break
            previous = refined
        total_fresh_ingredients = 0
        for lower, upper in refined:
            total_fresh_ingredients += (upper - lower) + 1
        return total_fresh_ingredients


if __name__ == "__main__":

    print("\n-------Answers-------\n")

    practise_solver = DayFiveSolver("day5/day5_example_input.txt")
    print(f"Part 1 practise: {practise_solver.calculate_fresh_ingredients_p1()}\n")

    final_solver = DayFiveSolver("day5/day5_input.txt")
    print(f"Part 1 real: {final_solver.calculate_fresh_ingredients_p1()}\n")

    practise_solver = DayFiveSolver("day5/day5_example_input.txt")
    print(f"Part 2 practise: {practise_solver.calculate_fresh_ingredients_p2()}\n")

    final_solver = DayFiveSolver("day5/day5_input.txt")
    print(f"Part 2 real: {final_solver.calculate_fresh_ingredients_p2()}\n")
