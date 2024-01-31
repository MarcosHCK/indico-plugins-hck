# OperationsPostComplete


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**merchant_op_id** | **str** |  | [optional] 
**terminal_id** | **str** |  | [optional] 
**amount** | [**FullOperationsOperationAmount**](FullOperationsOperationAmount.md) |  | [optional] 
**items** | [**List[OperationsPostCompleteItemsInner]**](OperationsPostCompleteItemsInner.md) |  | [optional] 

## Example

```python
from enzona_transfermovil.models.operations_post_complete import OperationsPostComplete

# TODO update the JSON string below
json = "{}"
# create an instance of OperationsPostComplete from a JSON string
operations_post_complete_instance = OperationsPostComplete.from_json(json)
# print the JSON string representation of the object
print OperationsPostComplete.to_json()

# convert the object into a dict
operations_post_complete_dict = operations_post_complete_instance.to_dict()
# create an instance of OperationsPostComplete from a dict
operations_post_complete_form_dict = operations_post_complete.from_dict(operations_post_complete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


