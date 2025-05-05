import unittest
import puzzle

class PuzzleRuleTests(unittest.TestCase):
    testdata = [
        ("|0", "012", True), ("|0", "120", False),
        ("0|", "120", True), ("0|", "012", False),
        ("12", "120", True), ("12", "210", False),
        ("20", "120", True), ("20", "102", False),
    ]
    illegal_testdata = [
        ("", "120"), ("0", "012"), ("120", "120"),
        ("01", "1"), ("01", ""),
    ]

    def test_mandatory_correct(self):
        for t in self.testdata:
            with self.subTest(rule=t[0], guess=t[1], expected=t[2]):
                result = puzzle.mandatory_correct(t[0], t[1])
                self.assertEqual(result, t[2])

    def test_forbidden_correct(self):
        for t in self.testdata:
            with self.subTest(rule=t[0], guess=t[1], expected=(not t[2])):
                result = puzzle.forbidden_correct(t[0], t[1])
                self.assertEqual(result, not t[2])

    def test_mandatory_correct_illegal_data(self):
        for t in self.illegal_testdata:
            with self.subTest(rule=t[0], guess=t[1]):
                result = puzzle.mandatory_correct(t[0], t[1])
                self.assertEqual(result, False)

    def test_forbidden_correct_illegal_data(self):
        for t in self.illegal_testdata:
            with self.subTest(rule=t[0], guess=t[1]):
                result = puzzle.forbidden_correct(t[0], t[1])
                self.assertEqual(result, False)

class PuzzleTests(unittest.TestCase):
    def test_create_all_rules(self):
        solution = "0123"
        mandatory, forbidden = puzzle.create_all_rules(solution)
        self.assertListEqual(sorted(mandatory), ["01", "12", "23", "3|", "|0"])
        self.assertListEqual(sorted(forbidden),
            ["02", "03", "0|", "10", "13", "1|", "20", "21", "2|", "30", "31", "32", "|1", "|2", "|3"])

    def test_all_solutions(self):
        result = list(puzzle.all_solutions(4, ""))
        self.assertListEqual(sorted(result),
            [
                "0123", "0132", "0213", "0231", "0312", "0321",
                "1023", "1032", "1203", "1230", "1302", "1320",
                "2013", "2031", "2103", "2130", "2301", "2310",
                "3012", "3021", "3102", "3120", "3201", "3210"
            ])

    def test_has_exactly_one_solution(self):
        self.assertEqual(puzzle.has_exactly_one_solution(
            4, [], []
        ), False)
        self.assertEqual(puzzle.has_exactly_one_solution(
            4, ["|0", "12"], ["0|", "20"]
        ), False)
        self.assertEqual(puzzle.has_exactly_one_solution(
            4, ["|0", "12"], ["0|", "23"]
        ), True)
        self.assertEqual(puzzle.has_exactly_one_solution(
            4, ["12", "23", "01"], []
        ), True)
        self.assertEqual(puzzle.has_exactly_one_solution(
            4, [], ["03", "0|", "13", "20", "2|", "30", "31", "|1", "|3"]
        ), True)

    def test_create_puzzle(self):
        LENGTH: int = 4
        solution, mandatory, forbidden = puzzle.create_puzzle(LENGTH)
        self.assertEqual(len(solution), LENGTH)
        self.assertEqual(puzzle.has_exactly_one_solution(LENGTH, mandatory, forbidden), True)

    def test_create_puzzle_length(self):
        self.assertRaises(Exception, puzzle.create_puzzle, 1)
        self.assertRaises(Exception, puzzle.create_puzzle, 10)

if __name__ == "__main__":
    unittest.main()
