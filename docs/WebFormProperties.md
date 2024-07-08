# WebFormProperties

General information about the web form that is consistent across versions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User friendly Form name. This can be set via UI and/or API. | [optional] 
**is_private_access** | **bool** | When a form is private, the Player will not be accessible via its URL unless a valid instance token is provided | [optional] 

## Example

```python
from openapi_client.models.web_form_properties import WebFormProperties

# TODO update the JSON string below
json = "{}"
# create an instance of WebFormProperties from a JSON string
web_form_properties_instance = WebFormProperties.from_json(json)
# print the JSON string representation of the object
print(WebFormProperties.to_json())

# convert the object into a dict
web_form_properties_dict = web_form_properties_instance.to_dict()
# create an instance of WebFormProperties from a dict
web_form_properties_from_dict = WebFormProperties.from_dict(web_form_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


