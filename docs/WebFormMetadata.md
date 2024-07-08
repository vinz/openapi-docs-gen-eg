# WebFormMetadata

Form metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**WebFormSource**](WebFormSource.md) |  | [optional] 
**owner** | [**WebFormUserInfo**](WebFormUserInfo.md) |  | [optional] 
**sender** | [**WebFormUserInfo**](WebFormUserInfo.md) |  | [optional] 
**last_modified_by** | [**WebFormUserInfo**](WebFormUserInfo.md) |  | [optional] 
**form_content_modified_by** | [**WebFormUserInfo**](WebFormUserInfo.md) |  | [optional] 
**form_properties_modified_by** | [**WebFormUserInfo**](WebFormUserInfo.md) |  | [optional] 
**last_published_by** | [**WebFormUserInfo**](WebFormUserInfo.md) |  | [optional] 
**last_enabled_by** | [**WebFormUserInfo**](WebFormUserInfo.md) |  | [optional] 
**last_disabled_by** | [**WebFormUserInfo**](WebFormUserInfo.md) |  | [optional] 
**archived_date_time** | **datetime** | The last time the web form was archived | [optional] 
**created_date_time** | **datetime** | Track the time the web form was created | [optional] 
**last_modified_date_time** | **datetime** | The last time anything was modified on the form | [optional] 
**form_content_modified_date_time** | **datetime** | Track the last time web form content changed. | [optional] 
**form_properties_modified_date_time** | **datetime** | Track the last time the form properties changed. | [optional] 
**last_published_date_time** | **datetime** | Track the last time a draft version was published to active | [optional] 
**last_enabled_date_time** | **datetime** | Track the last time the form was enabled | [optional] 
**last_disabled_date_time** | **datetime** | Track the last time the form was disabled | [optional] 
**last_sender_consent_date_time** | **datetime** | Track the last time a user added their consent for the form. | [optional] 
**published_slug** | **str** | The public friendly slug that is used to access the form from the player | [optional] 
**published_component_names** | [**Dict[str, WebFormComponentType]**](WebFormComponentType.md) | A dictionary containing the mapping of component names to their respective component types for all the published components. | [optional] 

## Example

```python
from openapi_client.models.web_form_metadata import WebFormMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WebFormMetadata from a JSON string
web_form_metadata_instance = WebFormMetadata.from_json(json)
# print the JSON string representation of the object
print(WebFormMetadata.to_json())

# convert the object into a dict
web_form_metadata_dict = web_form_metadata_instance.to_dict()
# create an instance of WebFormMetadata from a dict
web_form_metadata_from_dict = WebFormMetadata.from_dict(web_form_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


