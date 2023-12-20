# PaymentSummaryInfoOperationsOperationAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**details** | [**PaymentSummaryInfoOperationsOperationAmountDetails**](PaymentSummaryInfoOperationsOperationAmountDetails.md) |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payment_summary_info_operations_operation_amount import PaymentSummaryInfoOperationsOperationAmount

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSummaryInfoOperationsOperationAmount from a JSON string
payment_summary_info_operations_operation_amount_instance = PaymentSummaryInfoOperationsOperationAmount.from_json(json)
# print the JSON string representation of the object
print PaymentSummaryInfoOperationsOperationAmount.to_json()

# convert the object into a dict
payment_summary_info_operations_operation_amount_dict = payment_summary_info_operations_operation_amount_instance.to_dict()
# create an instance of PaymentSummaryInfoOperationsOperationAmount from a dict
payment_summary_info_operations_operation_amount_form_dict = payment_summary_info_operations_operation_amount.from_dict(payment_summary_info_operations_operation_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


