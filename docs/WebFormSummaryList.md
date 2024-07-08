# WebFormSummaryList

A list of web form summary items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WebFormSummary]**](WebFormSummary.md) | Array of web form items with each containing summary. | [optional] 
**result_set_size** | **float** | Result set size for current page | [optional] 
**total_set_size** | **float** | Total result set size | [optional] 
**start_position** | **float** | Starting position of fields returned for the current page | [optional] 
**end_position** | **float** | Ending position of fields returned for the current page | [optional] 
**next_url** | **str** | Url for the next page of results | [optional] 
**previous_url** | **str** | Url for the previous page of results | [optional] 

## Example

```python
from openapi_client.models.web_form_summary_list import WebFormSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of WebFormSummaryList from a JSON string
web_form_summary_list_instance = WebFormSummaryList.from_json(json)
# print the JSON string representation of the object
print(WebFormSummaryList.to_json())

# convert the object into a dict
web_form_summary_list_dict = web_form_summary_list_instance.to_dict()
# create an instance of WebFormSummaryList from a dict
web_form_summary_list_from_dict = WebFormSummaryList.from_dict(web_form_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


