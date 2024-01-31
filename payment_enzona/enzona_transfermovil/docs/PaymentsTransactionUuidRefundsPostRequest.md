# PaymentsTransactionUuidRefundsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**commerce_refund_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payments_transaction_uuid_refunds_post_request import PaymentsTransactionUuidRefundsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentsTransactionUuidRefundsPostRequest from a JSON string
payments_transaction_uuid_refunds_post_request_instance = PaymentsTransactionUuidRefundsPostRequest.from_json(json)
# print the JSON string representation of the object
print PaymentsTransactionUuidRefundsPostRequest.to_json()

# convert the object into a dict
payments_transaction_uuid_refunds_post_request_dict = payments_transaction_uuid_refunds_post_request_instance.to_dict()
# create an instance of PaymentsTransactionUuidRefundsPostRequest from a dict
payments_transaction_uuid_refunds_post_request_form_dict = payments_transaction_uuid_refunds_post_request.from_dict(payments_transaction_uuid_refunds_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


