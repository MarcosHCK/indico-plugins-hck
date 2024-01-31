# FullOperationsOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**merchant_op_id** | **str** |  | [optional] 
**terminal_id** | **str** |  | [optional] 
**amount** | [**FullOperationsOperationAmount**](FullOperationsOperationAmount.md) |  | [optional] 
**items** | [**List[FullOperationsOperationItemsInner]**](FullOperationsOperationItemsInner.md) |  | [optional] 

## Example

```python
from enzona_transfermovil.models.full_operations_operation import FullOperationsOperation

# TODO update the JSON string below
json = "{}"
# create an instance of FullOperationsOperation from a JSON string
full_operations_operation_instance = FullOperationsOperation.from_json(json)
# print the JSON string representation of the object
print FullOperationsOperation.to_json()

# convert the object into a dict
full_operations_operation_dict = full_operations_operation_instance.to_dict()
# create an instance of FullOperationsOperation from a dict
full_operations_operation_form_dict = full_operations_operation.from_dict(full_operations_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


