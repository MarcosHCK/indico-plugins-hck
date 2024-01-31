# FullOperationsOperationAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**details** | [**FullOperationsOperationAmountDetails**](FullOperationsOperationAmountDetails.md) |  | [optional] 

## Example

```python
from enzona_transfermovil.models.full_operations_operation_amount import FullOperationsOperationAmount

# TODO update the JSON string below
json = "{}"
# create an instance of FullOperationsOperationAmount from a JSON string
full_operations_operation_amount_instance = FullOperationsOperationAmount.from_json(json)
# print the JSON string representation of the object
print FullOperationsOperationAmount.to_json()

# convert the object into a dict
full_operations_operation_amount_dict = full_operations_operation_amount_instance.to_dict()
# create an instance of FullOperationsOperationAmount from a dict
full_operations_operation_amount_form_dict = full_operations_operation_amount.from_dict(full_operations_operation_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


