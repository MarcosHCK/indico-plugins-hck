# PaymentsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**items** | [**List[PaymentsPostRequestItemsInner]**](PaymentsPostRequestItemsInner.md) |  | [optional] 
**merchant_op_id** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**return_url** | **str** |  | [optional] 
**cancel_url** | **str** |  | [optional] 
**terminal_id** | **str** |  | [optional] 
**merchant_uuid** | **str** |  | [optional] 
**valid_time** | **float** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payments_post_request import PaymentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentsPostRequest from a JSON string
payments_post_request_instance = PaymentsPostRequest.from_json(json)
# print the JSON string representation of the object
print PaymentsPostRequest.to_json()

# convert the object into a dict
payments_post_request_dict = payments_post_request_instance.to_dict()
# create an instance of PaymentsPostRequest from a dict
payments_post_request_form_dict = payments_post_request.from_dict(payments_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


