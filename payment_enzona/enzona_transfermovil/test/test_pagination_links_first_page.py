# coding: utf-8

"""
    TransferMovilAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from enzona_transfermovil.models.pagination_links_first_page import PaginationLinksFirstPage

class TestPaginationLinksFirstPage(unittest.TestCase):
    """PaginationLinksFirstPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginationLinksFirstPage:
        """Test PaginationLinksFirstPage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginationLinksFirstPage`
        """
        model = PaginationLinksFirstPage()
        if include_optional:
            return PaginationLinksFirstPage(
                href = ''
            )
        else:
            return PaginationLinksFirstPage(
        )
        """

    def testPaginationLinksFirstPage(self):
        """Test PaginationLinksFirstPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
