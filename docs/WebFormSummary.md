# WebFormSummary

An object that summarizes an instance of a form that can be used to display a listing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for a Web Form that is consistent for it&#39;s lifetime | [optional] 
**account_id** | **str** | Account identifier in which the web form resides | [optional] 
**is_published** | **bool** | Has the form been published | [optional] 
**is_enabled** | **bool** | Is the form currently enabled and available for data collection | [optional] 
**has_draft_changes** | **bool** | Does the form have draft changes that need to be published? | [optional] 
**form_state** | [**WebFormState**](WebFormState.md) |  | [optional] 
**form_properties** | [**WebFormProperties**](WebFormProperties.md) |  | [optional] 
**form_metadata** | [**WebFormMetadata**](WebFormMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.web_form_summary import WebFormSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WebFormSummary from a JSON string
web_form_summary_instance = WebFormSummary.from_json(json)
# print the JSON string representation of the object
print(WebFormSummary.to_json())

# convert the object into a dict
web_form_summary_dict = web_form_summary_instance.to_dict()
# create an instance of WebFormSummary from a dict
web_form_summary_from_dict = WebFormSummary.from_dict(web_form_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


