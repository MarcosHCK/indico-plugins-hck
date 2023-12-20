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

from enzona_transfermovil.models.payment_full_operations import PaymentFullOperations

class TestPaymentFullOperations(unittest.TestCase):
    """PaymentFullOperations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentFullOperations:
        """Test PaymentFullOperations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentFullOperations`
        """
        model = PaymentFullOperations()
        if include_optional:
            return PaymentFullOperations(
                transaction_uuid = 'f89c79c8dfbd43939cdc43cf47b1ee47',
                currency = 'CUP',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status_code = 56,
                status_denom = 'Pendiente',
                description = 'Payment description',
                invoice_number = 56,
                merchant_op_id = '1135',
                terminal_id = 56,
                amount = enzona_transfermovil.models.amount_operations.amountOperations(
                    total = 56, 
                    details = enzona_transfermovil.models.details_operations.detailsOperations(
                        shipping = 56, 
                        tax = 56, 
                        discount = 1.337, 
                        tip = 1.337, ), ),
                items = [
                    enzona_transfermovil.models.items_operations.itemsOperations(
                        description = 'Pan', 
                        quantity = 56, 
                        price = 56, 
                        tax = 56, 
                        name = 'Arroz a la Cubana', )
                    ],
                links = [
                    enzona_transfermovil.models.links_schema.linksSchema(
                        rel = 'confirm', 
                        method = 'REDIRECT', 
                        href = 'https://enzona.xetid.cu/checkout/1940841ec89d4f32aef06c813825920b/login', )
                    ]
            )
        else:
            return PaymentFullOperations(
        )
        """

    def testPaymentFullOperations(self):
        """Test PaymentFullOperations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
