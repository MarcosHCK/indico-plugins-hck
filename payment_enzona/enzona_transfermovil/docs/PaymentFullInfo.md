# PaymentFullInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**state** | **str** |  | [optional] 
**payer** | [**PaymentFullInfoPayer**](PaymentFullInfoPayer.md) |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payment_full_info import PaymentFullInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFullInfo from a JSON string
payment_full_info_instance = PaymentFullInfo.from_json(json)
# print the JSON string representation of the object
print PaymentFullInfo.to_json()

# convert the object into a dict
payment_full_info_dict = payment_full_info_instance.to_dict()
# create an instance of PaymentFullInfo from a dict
payment_full_info_form_dict = payment_full_info.from_dict(payment_full_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


