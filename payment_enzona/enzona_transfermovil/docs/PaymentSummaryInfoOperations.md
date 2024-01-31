# PaymentSummaryInfoOperations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**PaymentSummaryInfoOperationsOperation**](PaymentSummaryInfoOperationsOperation.md) |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payment_summary_info_operations import PaymentSummaryInfoOperations

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSummaryInfoOperations from a JSON string
payment_summary_info_operations_instance = PaymentSummaryInfoOperations.from_json(json)
# print the JSON string representation of the object
print PaymentSummaryInfoOperations.to_json()

# convert the object into a dict
payment_summary_info_operations_dict = payment_summary_info_operations_instance.to_dict()
# create an instance of PaymentSummaryInfoOperations from a dict
payment_summary_info_operations_form_dict = payment_summary_info_operations.from_dict(payment_summary_info_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


