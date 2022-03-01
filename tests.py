import unittest
from main import remove_head_foot


class Test(unittest.TestCase):
    def test(self):
        header = 10
        footer = 15
        buffer = []

        with open('4ebbbebb46fab13cadcac3a1b0041b4c.txt', 'r') as f:
            for _ in range(header):
                f.readline()

            for _ in range(footer):
                buffer.append(f.readline())

            for line in f:
                buffer.append(line)
                line = buffer.pop(0)

                # do stuff to line
                print(line)
        actual = line
        with open('expected_results/4ebbbebb46fab13cadcac3a1b0041b4c.txt', 'r') as f:
            file = f.readline()
        expected = file
        self.assertEqual(actual, expected)