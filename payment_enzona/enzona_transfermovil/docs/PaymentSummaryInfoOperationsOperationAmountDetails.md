# PaymentSummaryInfoOperationsOperationAmountDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tip** | **str** |  | [optional] 
**tax** | **int** |  | [optional] 
**shipping** | **int** |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payment_summary_info_operations_operation_amount_details import PaymentSummaryInfoOperationsOperationAmountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSummaryInfoOperationsOperationAmountDetails from a JSON string
payment_summary_info_operations_operation_amount_details_instance = PaymentSummaryInfoOperationsOperationAmountDetails.from_json(json)
# print the JSON string representation of the object
print PaymentSummaryInfoOperationsOperationAmountDetails.to_json()

# convert the object into a dict
payment_summary_info_operations_operation_amount_details_dict = payment_summary_info_operations_operation_amount_details_instance.to_dict()
# create an instance of PaymentSummaryInfoOperationsOperationAmountDetails from a dict
payment_summary_info_operations_operation_amount_details_form_dict = payment_summary_info_operations_operation_amount_details.from_dict(payment_summary_info_operations_operation_amount_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


