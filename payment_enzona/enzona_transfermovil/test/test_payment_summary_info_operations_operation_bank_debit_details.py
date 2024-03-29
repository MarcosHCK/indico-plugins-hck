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

from enzona_transfermovil.models.payment_summary_info_operations_operation_bank_debit_details import PaymentSummaryInfoOperationsOperationBankDebitDetails

class TestPaymentSummaryInfoOperationsOperationBankDebitDetails(unittest.TestCase):
    """PaymentSummaryInfoOperationsOperationBankDebitDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentSummaryInfoOperationsOperationBankDebitDetails:
        """Test PaymentSummaryInfoOperationsOperationBankDebitDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentSummaryInfoOperationsOperationBankDebitDetails`
        """
        model = PaymentSummaryInfoOperationsOperationBankDebitDetails()
        if include_optional:
            return PaymentSummaryInfoOperationsOperationBankDebitDetails(
                trans_amount = '',
                currency = 'CUP',
                exchange_rate = 56,
                discount = 56
            )
        else:
            return PaymentSummaryInfoOperationsOperationBankDebitDetails(
        )
        """

    def testPaymentSummaryInfoOperationsOperationBankDebitDetails(self):
        """Test PaymentSummaryInfoOperationsOperationBankDebitDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
