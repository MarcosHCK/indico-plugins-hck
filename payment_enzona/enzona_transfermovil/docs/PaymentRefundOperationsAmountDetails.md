# PaymentRefundOperationsAmountDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping** | **int** |  | [optional] 
**tax** | **int** |  | [optional] 
**discount** | **float** |  | [optional] 
**tip** | **float** |  | [optional] 
**refunded** | **int** |  | [optional] 
**total_refunded** | **int** |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payment_refund_operations_amount_details import PaymentRefundOperationsAmountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRefundOperationsAmountDetails from a JSON string
payment_refund_operations_amount_details_instance = PaymentRefundOperationsAmountDetails.from_json(json)
# print the JSON string representation of the object
print PaymentRefundOperationsAmountDetails.to_json()

# convert the object into a dict
payment_refund_operations_amount_details_dict = payment_refund_operations_amount_details_instance.to_dict()
# create an instance of PaymentRefundOperationsAmountDetails from a dict
payment_refund_operations_amount_details_form_dict = payment_refund_operations_amount_details.from_dict(payment_refund_operations_amount_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


