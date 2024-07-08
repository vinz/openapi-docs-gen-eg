# WebFormInstanceList

A list of web form instance items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WebFormInstance]**](WebFormInstance.md) | Array of web form instance items. | [optional] 

## Example

```python
from openapi_client.models.web_form_instance_list import WebFormInstanceList

# TODO update the JSON string below
json = "{}"
# create an instance of WebFormInstanceList from a JSON string
web_form_instance_list_instance = WebFormInstanceList.from_json(json)
# print the JSON string representation of the object
print(WebFormInstanceList.to_json())

# convert the object into a dict
web_form_instance_list_dict = web_form_instance_list_instance.to_dict()
# create an instance of WebFormInstanceList from a dict
web_form_instance_list_from_dict = WebFormInstanceList.from_dict(web_form_instance_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


