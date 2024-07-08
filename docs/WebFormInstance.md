# WebFormInstance

An object that contains the Web Form Instance required to render it  and its metadata such as created by, created time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_url** | **str** | The url used to render the web form instance. | [optional] 
**instance_token** | **str** | Unique token associated with an instance that is required to render the form instance. This token is valid for 5 minutes after which it needs to be refreshed using refreshToken api | [optional] 
**token_expiration_date_time** | **datetime** | The datetime after which the token is expired and form instance is inaccessible. | [optional] 
**id** | **str** | Unique identifier for a Web Form Instance that is consistent until its expiration | 
**form_id** | **str** | Unique identifier for a Web Form that is consistent for it&#39;s lifetime | [optional] 
**account_id** | **str** | Account identifier in which the web form resides | [optional] 
**client_user_id** | **str** | A unique identifier for a user that should originate from client&#39;s system. This value can be anything your backend system would use to track individual form instances. Examples include employee IDs, email addresses, surrogate key values, etc. | [optional] 
**tags** | **List[str]** | List of tags provided by the user with each request. This field is optional. | [optional] 
**status** | [**InstanceStatus**](InstanceStatus.md) |  | [optional] 
**envelopes** | [**List[WebFormInstanceEnvelopesInner]**](WebFormInstanceEnvelopesInner.md) | The associated envelope that is created when the instance is submitted | [optional] 
**instance_metadata** | [**WebFormInstanceMetadata**](WebFormInstanceMetadata.md) |  | [optional] 
**form_values** | **Dict[str, object]** | Key-value pairs (where key is the component name and value is the form value) used to create a form instance. For key of type TextBox, Email, Date, Select and RadioButtonGroup the value is of string type. For key of type Number, the value is of number type. For key of type of CheckboxGroup, the value is of type array of string. | [optional] 

## Example

```python
from openapi_client.models.web_form_instance import WebFormInstance

# TODO update the JSON string below
json = "{}"
# create an instance of WebFormInstance from a JSON string
web_form_instance_instance = WebFormInstance.from_json(json)
# print the JSON string representation of the object
print(WebFormInstance.to_json())

# convert the object into a dict
web_form_instance_dict = web_form_instance_instance.to_dict()
# create an instance of WebFormInstance from a dict
web_form_instance_from_dict = WebFormInstance.from_dict(web_form_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


