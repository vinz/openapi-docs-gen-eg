# CreateInstanceRequestBody

Request body containing properties that will be used to create instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_values** | **Dict[str, object]** | Key-value pairs (where key is the component name and value is the form value) used to create a form instance. For key of type TextBox, Email, Date, Select and RadioButtonGroup the value is of string type. For key of type Number, the value is of number type. For key of type of CheckboxGroup, the value is of type array of string. | [optional] 
**client_user_id** | **str** | A unique identifier for a user that should originate from client&#39;s system. This value can be anything your backend system would use to track individual form instances. Examples include employee IDs, email addresses, surrogate key values, etc. | 
**authentication_instant** | **str** | A sender-generated value that indicates the date and time that the signer was authenticated. | [optional] 
**authentication_method** | [**AuthenticationMethod**](AuthenticationMethod.md) |  | [optional] 
**assertion_id** | **str** | A unique identifier of the authentication event executed by the client application. | [optional] 
**security_domain** | **str** | The domain in which the user authenticated. | [optional] 
**return_url** | **str** | The url to which the user is redirected after the signing is completed | [optional] 
**expiration_offset** | **int** | Specify the number of hours after which the form instance expires. For example, if the form expiration is set to 5 days, you should specify 120. The default value is 720 hours (30 days). | [optional] 
**tags** | **List[str]** | List of tags provided by the user with each request. This field is optional. | [optional] 

## Example

```python
from openapi_client.models.create_instance_request_body import CreateInstanceRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInstanceRequestBody from a JSON string
create_instance_request_body_instance = CreateInstanceRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreateInstanceRequestBody.to_json())

# convert the object into a dict
create_instance_request_body_dict = create_instance_request_body_instance.to_dict()
# create an instance of CreateInstanceRequestBody from a dict
create_instance_request_body_from_dict = CreateInstanceRequestBody.from_dict(create_instance_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


