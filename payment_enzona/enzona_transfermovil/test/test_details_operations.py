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

from enzona_transfermovil.models.details_operations import DetailsOperations

class TestDetailsOperations(unittest.TestCase):
    """DetailsOperations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DetailsOperations:
        """Test DetailsOperations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DetailsOperations`
        """
        model = DetailsOperations()
        if include_optional:
            return DetailsOperations(
                shipping = 56,
                tax = 56,
                discount = 1.337,
                tip = 1.337
            )
        else:
            return DetailsOperations(
        )
        """

    def testDetailsOperations(self):
        """Test DetailsOperations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
