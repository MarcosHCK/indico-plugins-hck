# PaymentsPostRequestItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**price** | **float** |  | [optional] 
**tax** | **float** |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payments_post_request_items_inner import PaymentsPostRequestItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentsPostRequestItemsInner from a JSON string
payments_post_request_items_inner_instance = PaymentsPostRequestItemsInner.from_json(json)
# print the JSON string representation of the object
print PaymentsPostRequestItemsInner.to_json()

# convert the object into a dict
payments_post_request_items_inner_dict = payments_post_request_items_inner_instance.to_dict()
# create an instance of PaymentsPostRequestItemsInner from a dict
payments_post_request_items_inner_form_dict = payments_post_request_items_inner.from_dict(payments_post_request_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


