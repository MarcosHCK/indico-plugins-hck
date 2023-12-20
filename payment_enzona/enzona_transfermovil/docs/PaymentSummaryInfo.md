# PaymentSummaryInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**state** | **str** |  | [optional] 
**operations** | [**PaymentSummaryInfoOperations**](PaymentSummaryInfoOperations.md) |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payment_summary_info import PaymentSummaryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSummaryInfo from a JSON string
payment_summary_info_instance = PaymentSummaryInfo.from_json(json)
# print the JSON string representation of the object
print PaymentSummaryInfo.to_json()

# convert the object into a dict
payment_summary_info_dict = payment_summary_info_instance.to_dict()
# create an instance of PaymentSummaryInfo from a dict
payment_summary_info_form_dict = payment_summary_info.from_dict(payment_summary_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


