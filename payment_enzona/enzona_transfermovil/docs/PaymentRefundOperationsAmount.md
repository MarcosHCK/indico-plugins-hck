# PaymentRefundOperationsAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**details** | [**PaymentRefundOperationsAmountDetails**](PaymentRefundOperationsAmountDetails.md) |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payment_refund_operations_amount import PaymentRefundOperationsAmount

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRefundOperationsAmount from a JSON string
payment_refund_operations_amount_instance = PaymentRefundOperationsAmount.from_json(json)
# print the JSON string representation of the object
print PaymentRefundOperationsAmount.to_json()

# convert the object into a dict
payment_refund_operations_amount_dict = payment_refund_operations_amount_instance.to_dict()
# create an instance of PaymentRefundOperationsAmount from a dict
payment_refund_operations_amount_form_dict = payment_refund_operations_amount.from_dict(payment_refund_operations_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


