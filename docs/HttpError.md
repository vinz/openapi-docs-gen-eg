# HttpError

An error occurred while processing a request. Source - https://www.baeldung.com/rest-api-error-handling-best-practices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | A granular, human and computer readable code indicating more deeply what error occurred. | [optional] 
**message** | **str** | A human-readable description of the error, meant for developers to store for their review. | [optional] 

## Example

```python
from openapi_client.models.http_error import HttpError

# TODO update the JSON string below
json = "{}"
# create an instance of HttpError from a JSON string
http_error_instance = HttpError.from_json(json)
# print the JSON string representation of the object
print(HttpError.to_json())

# convert the object into a dict
http_error_dict = http_error_instance.to_dict()
# create an instance of HttpError from a dict
http_error_from_dict = HttpError.from_dict(http_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


