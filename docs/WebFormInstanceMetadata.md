# WebFormInstanceMetadata

Web Form Instance metadata containing information like created by, created time, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_date_time** | **datetime** | The datetime after which the Web Form Instance is inaccessible. | 
**created_date_time** | **datetime** | The dateTime when the Web Form Instance is created. | 
**created_by** | [**WebFormUserInfo**](WebFormUserInfo.md) |  | 
**last_modified_date_time** | **datetime** | The dateTime when the Web Form Instance is last modified. | [optional] 
**last_modified_by** | [**WebFormUserInfo**](WebFormUserInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.web_form_instance_metadata import WebFormInstanceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WebFormInstanceMetadata from a JSON string
web_form_instance_metadata_instance = WebFormInstanceMetadata.from_json(json)
# print the JSON string representation of the object
print(WebFormInstanceMetadata.to_json())

# convert the object into a dict
web_form_instance_metadata_dict = web_form_instance_metadata_instance.to_dict()
# create an instance of WebFormInstanceMetadata from a dict
web_form_instance_metadata_from_dict = WebFormInstanceMetadata.from_dict(web_form_instance_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


