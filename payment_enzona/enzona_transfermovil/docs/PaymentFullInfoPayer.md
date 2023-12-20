# PaymentFullInfoPayer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer_info** | [**PaymentFullInfoPayerPayerInfo**](PaymentFullInfoPayerPayerInfo.md) |  | [optional] 

## Example

```python
from enzona_transfermovil.models.payment_full_info_payer import PaymentFullInfoPayer

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFullInfoPayer from a JSON string
payment_full_info_payer_instance = PaymentFullInfoPayer.from_json(json)
# print the JSON string representation of the object
print PaymentFullInfoPayer.to_json()

# convert the object into a dict
payment_full_info_payer_dict = payment_full_info_payer_instance.to_dict()
# create an instance of PaymentFullInfoPayer from a dict
payment_full_info_payer_form_dict = payment_full_info_payer.from_dict(payment_full_info_payer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


