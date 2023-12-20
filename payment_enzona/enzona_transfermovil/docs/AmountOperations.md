# AmountOperations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**details** | [**DetailsOperations**](DetailsOperations.md) |  | [optional] 

## Example

```python
from enzona_transfermovil.models.amount_operations import AmountOperations

# TODO update the JSON string below
json = "{}"
# create an instance of AmountOperations from a JSON string
amount_operations_instance = AmountOperations.from_json(json)
# print the JSON string representation of the object
print AmountOperations.to_json()

# convert the object into a dict
amount_operations_dict = amount_operations_instance.to_dict()
# create an instance of AmountOperations from a dict
amount_operations_form_dict = amount_operations.from_dict(amount_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


