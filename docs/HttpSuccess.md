# HttpSuccess

A simple response indicating success when no extra data is needed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.http_success import HttpSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of HttpSuccess from a JSON string
http_success_instance = HttpSuccess.from_json(json)
# print the JSON string representation of the object
print(HttpSuccess.to_json())

# convert the object into a dict
http_success_dict = http_success_instance.to_dict()
# create an instance of HttpSuccess from a dict
http_success_from_dict = HttpSuccess.from_dict(http_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


