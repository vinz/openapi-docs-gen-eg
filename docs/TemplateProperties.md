# TemplateProperties

Information about a DocuSign template that will be used to seed a web form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_template_id** | **str** |  | [optional] 
**cloned_template_id** | **str** |  | [optional] 
**imported_date_time** | **datetime** | Track the time of assignment of Template information to the Form. | [optional] 
**recipient_ids** | **List[str]** | Track mapped recipients on Template. | [optional] 

## Example

```python
from openapi_client.models.template_properties import TemplateProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateProperties from a JSON string
template_properties_instance = TemplateProperties.from_json(json)
# print the JSON string representation of the object
print(TemplateProperties.to_json())

# convert the object into a dict
template_properties_dict = template_properties_instance.to_dict()
# create an instance of TemplateProperties from a dict
template_properties_from_dict = TemplateProperties.from_dict(template_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


