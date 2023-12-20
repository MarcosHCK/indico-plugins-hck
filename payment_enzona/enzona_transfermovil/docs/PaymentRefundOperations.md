# PaymentRefundOperations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_uuid** | **str** |  | [optional] 
**status_code** | **str** |  | [optional] 
**status_denom** | **str** |  | [optional] 
**transaction_created_at** | **str** |  | [optional] 
**transaction_updated_at** | **str** |  | [optional] 
**transaction_signature** | **str** |  | [optional] 
**amount** | [**PaymentRefundOperationsAmount**](PaymentRefundOperationsAmount.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**transaction_description** | **str** |  | [optional] 
**transaction_denom** | **str** |  | [optional] 
**transaction_code** | **str** |  | [optional] 
**terminal_id** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**lastname** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**items** | [**List[ItemsOperations]**](ItemsOperations.md) |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payment_refund_operations import PaymentRefundOperations

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRefundOperations from a JSON string
payment_refund_operations_instance = PaymentRefundOperations.from_json(json)
# print the JSON string representation of the object
print PaymentRefundOperations.to_json()

# convert the object into a dict
payment_refund_operations_dict = payment_refund_operations_instance.to_dict()
# create an instance of PaymentRefundOperations from a dict
payment_refund_operations_form_dict = payment_refund_operations.from_dict(payment_refund_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


