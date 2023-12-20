# LinksSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rel** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from enzona_transfermovil.models.links_schema import LinksSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LinksSchema from a JSON string
links_schema_instance = LinksSchema.from_json(json)
# print the JSON string representation of the object
print LinksSchema.to_json()

# convert the object into a dict
links_schema_dict = links_schema_instance.to_dict()
# create an instance of LinksSchema from a dict
links_schema_form_dict = links_schema.from_dict(links_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


