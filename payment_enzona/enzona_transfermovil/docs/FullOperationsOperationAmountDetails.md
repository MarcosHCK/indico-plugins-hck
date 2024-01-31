# FullOperationsOperationAmountDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping** | **int** |  | [optional] 
**tax** | **int** |  | [optional] 
**discount** | **int** |  | [optional] 
**tip** | **int** |  | [optional] 

## Example

```python
from enzona_transfermovil.models.full_operations_operation_amount_details import FullOperationsOperationAmountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FullOperationsOperationAmountDetails from a JSON string
full_operations_operation_amount_details_instance = FullOperationsOperationAmountDetails.from_json(json)
# print the JSON string representation of the object
print FullOperationsOperationAmountDetails.to_json()

# convert the object into a dict
full_operations_operation_amount_details_dict = full_operations_operation_amount_details_instance.to_dict()
# create an instance of FullOperationsOperationAmountDetails from a dict
full_operations_operation_amount_details_form_dict = full_operations_operation_amount_details.from_dict(full_operations_operation_amount_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


