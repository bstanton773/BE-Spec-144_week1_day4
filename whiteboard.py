import unittest

# Pair of gloves
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of 
# pair of gloves you can constitute from the gloves you have in your drawer.

# Given an array describing the color of each glove, return the number of pairs you can constitute, 
# assuming that only gloves of the same color can form pairs.

# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2 (1 red pair + 1 blue pair)

# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)


def solution(gloves):
    glove_count = {}
    for color in gloves:
        glove_count[color] = glove_count.get(color, 0) + 1
    pair_count = 0
    for color, count in glove_count.items():
        pair_count += count // 2
    return pair_count

def solution(gloves):
    unique_gloves = set(gloves)
    pair_count = 0
    for glove in unique_gloves:
        pair_count += gloves.count(glove) // 2
    return pair_count


class GlovePairsTestCase(unittest.TestCase):
    def test_example_one(self):
        input_gloves = ["red", "green", "red", "blue", "blue"]
        assert solution(input_gloves) == 2

    def test_example_two(self):
        input_gloves = ["red", "red", "red", "red", "red", "red"]
        assert solution(input_gloves) == 3

    def test_empty_input(self):
        input_gloves = []
        assert solution(input_gloves) == 0

    def test_single_color(self):
        input_gloves = ["blue", "blue", "blue"]
        assert solution(input_gloves) == 1

    def test_more_colors(self):
        input_gloves = ["yellow", "purple", "purple", "yellow", "pink", "pink", "purple", "yellow"]
        assert solution(input_gloves) == 3

    def test_no_pairs(self):
        input_gloves = ["red", "blue", "green", "purple", "yellow", "pink"]
        assert solution(input_gloves) == 0

if __name__ == '__main__':
    unittest.main()


