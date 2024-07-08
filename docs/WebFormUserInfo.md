# WebFormUserInfo

Information about a DocuSign system user. The user exists within the account associated with the form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | DocuSign User identifier | [optional] 
**user_name** | **str** | Name of the user that can be displayed in the user interface. | [optional] 

## Example

```python
from openapi_client.models.web_form_user_info import WebFormUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WebFormUserInfo from a JSON string
web_form_user_info_instance = WebFormUserInfo.from_json(json)
# print the JSON string representation of the object
print(WebFormUserInfo.to_json())

# convert the object into a dict
web_form_user_info_dict = web_form_user_info_instance.to_dict()
# create an instance of WebFormUserInfo from a dict
web_form_user_info_from_dict = WebFormUserInfo.from_dict(web_form_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


