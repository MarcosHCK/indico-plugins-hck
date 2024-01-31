# PaymentFullInfoPayerPayerInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**payer_id** | **str** |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payment_full_info_payer_payer_info import PaymentFullInfoPayerPayerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFullInfoPayerPayerInfo from a JSON string
payment_full_info_payer_payer_info_instance = PaymentFullInfoPayerPayerInfo.from_json(json)
# print the JSON string representation of the object
print PaymentFullInfoPayerPayerInfo.to_json()

# convert the object into a dict
payment_full_info_payer_payer_info_dict = payment_full_info_payer_payer_info_instance.to_dict()
# create an instance of PaymentFullInfoPayerPayerInfo from a dict
payment_full_info_payer_payer_info_form_dict = payment_full_info_payer_payer_info.from_dict(payment_full_info_payer_payer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


