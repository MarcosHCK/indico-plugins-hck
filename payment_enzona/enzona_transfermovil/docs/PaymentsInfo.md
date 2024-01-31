# PaymentsInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payments_info import PaymentsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentsInfo from a JSON string
payments_info_instance = PaymentsInfo.from_json(json)
# print the JSON string representation of the object
print PaymentsInfo.to_json()

# convert the object into a dict
payments_info_dict = payments_info_instance.to_dict()
# create an instance of PaymentsInfo from a dict
payments_info_form_dict = payments_info.from_dict(payments_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


