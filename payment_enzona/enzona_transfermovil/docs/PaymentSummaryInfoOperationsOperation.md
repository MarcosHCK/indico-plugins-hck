# PaymentSummaryInfoOperationsOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**PaymentSummaryInfoOperationsOperationAmount**](PaymentSummaryInfoOperationsOperationAmount.md) |  | [optional] 
**bank_debit_details** | [**PaymentSummaryInfoOperationsOperationBankDebitDetails**](PaymentSummaryInfoOperationsOperationBankDebitDetails.md) |  | [optional] 
**description** | **str** |  | [optional] 
**merchant_op_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payment_summary_info_operations_operation import PaymentSummaryInfoOperationsOperation

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSummaryInfoOperationsOperation from a JSON string
payment_summary_info_operations_operation_instance = PaymentSummaryInfoOperationsOperation.from_json(json)
# print the JSON string representation of the object
print PaymentSummaryInfoOperationsOperation.to_json()

# convert the object into a dict
payment_summary_info_operations_operation_dict = payment_summary_info_operations_operation_instance.to_dict()
# create an instance of PaymentSummaryInfoOperationsOperation from a dict
payment_summary_info_operations_operation_form_dict = payment_summary_info_operations_operation.from_dict(payment_summary_info_operations_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


