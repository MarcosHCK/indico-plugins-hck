# ItemsOperations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**price** | **int** |  | [optional] 
**tax** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from enzona_transfermovil.models.items_operations import ItemsOperations

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsOperations from a JSON string
items_operations_instance = ItemsOperations.from_json(json)
# print the JSON string representation of the object
print ItemsOperations.to_json()

# convert the object into a dict
items_operations_dict = items_operations_instance.to_dict()
# create an instance of ItemsOperations from a dict
items_operations_form_dict = items_operations.from_dict(items_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


