# WebFormContent

Container for the components map used during configuration and data collection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**components** | **Dict[str, Dict[str, object]]** | Key/value dictionary of components that represent the form | [optional] 
**is_standalone** | **bool** | Is the form a standalone form | [optional] 
**brand_id** | **str** | Brand Id for web form | [optional] 
**templates** | [**List[TemplateProperties]**](TemplateProperties.md) | Optional template information that will be used to seed the form. | [optional] 

## Example

```python
from openapi_client.models.web_form_content import WebFormContent

# TODO update the JSON string below
json = "{}"
# create an instance of WebFormContent from a JSON string
web_form_content_instance = WebFormContent.from_json(json)
# print the JSON string representation of the object
print(WebFormContent.to_json())

# convert the object into a dict
web_form_content_dict = web_form_content_instance.to_dict()
# create an instance of WebFormContent from a dict
web_form_content_from_dict = WebFormContent.from_dict(web_form_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


