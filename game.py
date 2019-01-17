import sys
import argparse
import unittest

from xpath_tester import XPathTester

queries_file_path = None

class Game(XPathTester):
    def __init__(self, *args):
        super(Game, self).__init__(queries_file_path, *args, dtd_file_path='game.dtd')

    def test_game(self):
        self.set_xml_file_path('game.xml')
        self.assert_query_output_equal(0, ['noodles', 'blaze', 'blaze'])
        self.assert_query_output_equal(1, ['Chad', 'Bruce'])
        self.assert_query_output_equal(2, ['Noodles'])
        self.assert_query_output_equal(3, ['Noodles', 'Blaze'])
        self.assert_query_output_equal(4, ['42'])
        self.assert_number_of_queries(5)

if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('queries_file_path')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    queries_file_path = args.queries_file_path

    sys.argv[1:] = args.unittest_args
    unittest.main()

