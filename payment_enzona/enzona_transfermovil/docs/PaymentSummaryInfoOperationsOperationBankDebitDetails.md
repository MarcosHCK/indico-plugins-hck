# PaymentSummaryInfoOperationsOperationBankDebitDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trans_amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**exchange_rate** | **int** |  | [optional] 
**discount** | **int** |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payment_summary_info_operations_operation_bank_debit_details import PaymentSummaryInfoOperationsOperationBankDebitDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSummaryInfoOperationsOperationBankDebitDetails from a JSON string
payment_summary_info_operations_operation_bank_debit_details_instance = PaymentSummaryInfoOperationsOperationBankDebitDetails.from_json(json)
# print the JSON string representation of the object
print PaymentSummaryInfoOperationsOperationBankDebitDetails.to_json()

# convert the object into a dict
payment_summary_info_operations_operation_bank_debit_details_dict = payment_summary_info_operations_operation_bank_debit_details_instance.to_dict()
# create an instance of PaymentSummaryInfoOperationsOperationBankDebitDetails from a dict
payment_summary_info_operations_operation_bank_debit_details_form_dict = payment_summary_info_operations_operation_bank_debit_details.from_dict(payment_summary_info_operations_operation_bank_debit_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


