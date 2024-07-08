# openapi_client.FormManagementApi

All URIs are relative to *https://apps.docusign.com/api/webforms/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_form**](FormManagementApi.md#get_form) | **GET** /accounts/{accountId}/forms/{formId} | Get Form
[**list_forms**](FormManagementApi.md#list_forms) | **GET** /accounts/{accountId}/forms | List Forms


# **get_form**
> WebForm get_form(account_id, form_id, state=state)

Get Form

Retrieves form information filter by form id and state. The `state` parameter is optional and can accept value from `draft, active`.

### Example

* OAuth Authentication (docusignAccessCode):

```python
import openapi_client
from openapi_client.models.web_form import WebForm
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apps.docusign.com/api/webforms/v1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://apps.docusign.com/api/webforms/v1.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FormManagementApi(api_client)
    account_id = 'account_id_example' # str | Account identifier in which the web form resides
    form_id = 'form_id_example' # str | Unique identifier for a web form that is consistent for it's lifetime
    state = 'draft' # str | The state of the web form configuration (optional) (default to 'draft')

    try:
        # Get Form
        api_response = api_instance.get_form(account_id, form_id, state=state)
        print("The response of FormManagementApi->get_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormManagementApi->get_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account identifier in which the web form resides | 
 **form_id** | **str**| Unique identifier for a web form that is consistent for it&#39;s lifetime | 
 **state** | **str**| The state of the web form configuration | [optional] [default to &#39;draft&#39;]

### Return type

[**WebForm**](WebForm.md)

### Authorization

[docusignAccessCode](../README.md#docusignAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web Form that represents a single active version with metadata |  -  |
**401** | The authentication information is either missing or invalid |  -  |
**404** | The requested resource was not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_forms**
> WebFormSummaryList list_forms(account_id, user_filter=user_filter, is_standalone=is_standalone, is_published=is_published, sort_by=sort_by, search=search, start_position=start_position, count=count)

List Forms

List all the forms for the active user that can be in an active or draft state

### Example

* OAuth Authentication (docusignAccessCode):

```python
import openapi_client
from openapi_client.models.web_form_summary_list import WebFormSummaryList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apps.docusign.com/api/webforms/v1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://apps.docusign.com/api/webforms/v1.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FormManagementApi(api_client)
    account_id = 'account_id_example' # str | Account identifier in which the webform resides
    user_filter = 'all' # str | Filter which forms are returned (optional) (default to 'all')
    is_standalone = True # bool | Is the form a standalone form (optional)
    is_published = True # bool | Has the form been published (optional)
    sort_by = 'sort_by_example' # str | Sort result set in mentioned sort property:order. Default is lastModifiedDateTime:desc. Default sort is descending if not mentioned. (optional)
    search = 'search_example' # str | Search through form names (optional)
    start_position = 'start_position_example' # str | Starting position for desired page of results. (optional)
    count = 'count_example' # str | Number of results to return per page. (optional)

    try:
        # List Forms
        api_response = api_instance.list_forms(account_id, user_filter=user_filter, is_standalone=is_standalone, is_published=is_published, sort_by=sort_by, search=search, start_position=start_position, count=count)
        print("The response of FormManagementApi->list_forms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormManagementApi->list_forms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account identifier in which the webform resides | 
 **user_filter** | **str**| Filter which forms are returned | [optional] [default to &#39;all&#39;]
 **is_standalone** | **bool**| Is the form a standalone form | [optional] 
 **is_published** | **bool**| Has the form been published | [optional] 
 **sort_by** | **str**| Sort result set in mentioned sort property:order. Default is lastModifiedDateTime:desc. Default sort is descending if not mentioned. | [optional] 
 **search** | **str**| Search through form names | [optional] 
 **start_position** | **str**| Starting position for desired page of results. | [optional] 
 **count** | **str**| Number of results to return per page. | [optional] 

### Return type

[**WebFormSummaryList**](WebFormSummaryList.md)

### Authorization

[docusignAccessCode](../README.md#docusignAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of forms assigned to the account |  -  |
**401** | The authentication information is either missing or invalid |  -  |
**403** | The requestor is not authorized |  -  |
**404** | The requested resource was not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

