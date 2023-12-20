# PaymentsPost200Response


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
from enzona_transfermovil.models.payments_post200_response import PaymentsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentsPost200Response from a JSON string
payments_post200_response_instance = PaymentsPost200Response.from_json(json)
# print the JSON string representation of the object
print PaymentsPost200Response.to_json()

# convert the object into a dict
payments_post200_response_dict = payments_post200_response_instance.to_dict()
# create an instance of PaymentsPost200Response from a dict
payments_post200_response_form_dict = payments_post200_response.from_dict(payments_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


