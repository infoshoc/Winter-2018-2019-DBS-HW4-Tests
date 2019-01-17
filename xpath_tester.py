from unittest import TestCase

from lxml import etree
from io import StringIO, BytesIO


class XPathTester(TestCase):
    def __init__(self, queries_file_path, *args, dtd_file_path=None, xml_file_path=None):
        super(XPathTester, self).__init__(*args)

        self.tree = None

        with open(queries_file_path, 'r') as file_handler:
            self.queries = file_handler.readlines()

        if dtd_file_path is not None:
            self.dtd = etree.DTD(dtd_file_path)
        else:
            self.dtd = None

        if xml_file_path is not None:
            self.set_xml_file_path(xml_file_path)

    def assert_query_output_equal(self, query, desired_output):
        if isinstance(query, int):
            query = self.queries[query]

        print('Executing {}'.format(query))
        actual_output = self.tree.xpath(query)
        super().assertEqual(actual_output, desired_output)

    def assert_number_of_queries(self, number_of_queries):
        super().assertEqual(len(self.queries), number_of_queries)

    def set_xml_file_path(self, xml_file_path):
        self.tree = etree.parse(xml_file_path)

        if self.dtd is not None:
            assert self.dtd.validate(self.tree), 'Invalid xml {}'.format(xml_file_path)
