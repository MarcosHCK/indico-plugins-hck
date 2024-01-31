# DetailsOperations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping** | **int** |  | [optional] 
**tax** | **int** |  | [optional] 
**discount** | **float** |  | [optional] 
**tip** | **float** |  | [optional] 

## Example

```python
from enzona_transfermovil.models.details_operations import DetailsOperations

# TODO update the JSON string below
json = "{}"
# create an instance of DetailsOperations from a JSON string
details_operations_instance = DetailsOperations.from_json(json)
# print the JSON string representation of the object
print DetailsOperations.to_json()

# convert the object into a dict
details_operations_dict = details_operations_instance.to_dict()
# create an instance of DetailsOperations from a dict
details_operations_form_dict = details_operations.from_dict(details_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


