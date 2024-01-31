# PaymentFullOperations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_uuid** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**status_code** | **int** |  | [optional] 
**status_denom** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**invoice_number** | **int** |  | [optional] 
**merchant_op_id** | **str** |  | [optional] 
**terminal_id** | **int** |  | [optional] 
**amount** | [**AmountOperations**](AmountOperations.md) |  | [optional] 
**items** | [**List[ItemsOperations]**](ItemsOperations.md) |  | [optional] 
**links** | [**List[LinksSchema]**](LinksSchema.md) |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payment_full_operations import PaymentFullOperations

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFullOperations from a JSON string
payment_full_operations_instance = PaymentFullOperations.from_json(json)
# print the JSON string representation of the object
print PaymentFullOperations.to_json()

# convert the object into a dict
payment_full_operations_dict = payment_full_operations_instance.to_dict()
# create an instance of PaymentFullOperations from a dict
payment_full_operations_form_dict = payment_full_operations.from_dict(payment_full_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


