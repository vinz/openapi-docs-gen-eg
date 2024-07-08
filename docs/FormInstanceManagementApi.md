# openapi_client.FormInstanceManagementApi

All URIs are relative to *https://apps.docusign.com/api/webforms/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_instance**](FormInstanceManagementApi.md#create_instance) | **POST** /accounts/{accountId}/forms/{formId}/instances | Creates an instance of the web form
[**get_instance**](FormInstanceManagementApi.md#get_instance) | **GET** /accounts/{accountId}/forms/{formId}/instances/{instanceId} | Get form instance
[**list_instances**](FormInstanceManagementApi.md#list_instances) | **GET** /accounts/{accountId}/forms/{formId}/instances | List instances
[**refresh_token**](FormInstanceManagementApi.md#refresh_token) | **POST** /accounts/{accountId}/forms/{formId}/instances/{instanceId}/refresh | Refreshes the instance token


# **create_instance**
> WebFormInstance create_instance(account_id, form_id, create_instance_body)

Creates an instance of the web form

Creates an instance of the web form.

### Example

* OAuth Authentication (docusignAccessCode):

```python
import openapi_client
from openapi_client.models.create_instance_request_body import CreateInstanceRequestBody
from openapi_client.models.web_form_instance import WebFormInstance
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
    api_instance = openapi_client.FormInstanceManagementApi(api_client)
    account_id = 'account_id_example' # str | Account identifier in which the web form resides
    form_id = 'form_id_example' # str | Unique identifier for a web form entity that is consistent for it's lifetime
    create_instance_body = openapi_client.CreateInstanceRequestBody() # CreateInstanceRequestBody | Request body containing properties that will be used to create instance.

    try:
        # Creates an instance of the web form
        api_response = api_instance.create_instance(account_id, form_id, create_instance_body)
        print("The response of FormInstanceManagementApi->create_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormInstanceManagementApi->create_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account identifier in which the web form resides | 
 **form_id** | **str**| Unique identifier for a web form entity that is consistent for it&#39;s lifetime | 
 **create_instance_body** | [**CreateInstanceRequestBody**](CreateInstanceRequestBody.md)| Request body containing properties that will be used to create instance. | 

### Return type

[**WebFormInstance**](WebFormInstance.md)

### Authorization

[docusignAccessCode](../README.md#docusignAccessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web Form Instance with metadata |  -  |
**400** | The form instance cannot be created, possibly due to validation failure. |  -  |
**401** | The authentication information is either missing or invalid |  -  |
**403** | The requestor is not authorized |  -  |
**404** | The requested resource is not found |  -  |
**500** | The service encountered an unexpected condition that prevented it from fulfilling the request |  -  |
**503** | service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance**
> WebFormInstance get_instance(account_id, form_id, instance_id)

Get form instance

Retrieves instance information filter by instance id

### Example

* OAuth Authentication (docusignAccessCode):

```python
import openapi_client
from openapi_client.models.web_form_instance import WebFormInstance
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
    api_instance = openapi_client.FormInstanceManagementApi(api_client)
    account_id = 'account_id_example' # str | Account identifier in which the web form resides
    form_id = 'form_id_example' # str | Unique identifier for a web form entity that is consistent for it's lifetime
    instance_id = 'instance_id_example' # str | Unique identifier for a Web Form Instance that is consistent until its expiration

    try:
        # Get form instance
        api_response = api_instance.get_instance(account_id, form_id, instance_id)
        print("The response of FormInstanceManagementApi->get_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormInstanceManagementApi->get_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account identifier in which the web form resides | 
 **form_id** | **str**| Unique identifier for a web form entity that is consistent for it&#39;s lifetime | 
 **instance_id** | **str**| Unique identifier for a Web Form Instance that is consistent until its expiration | 

### Return type

[**WebFormInstance**](WebFormInstance.md)

### Authorization

[docusignAccessCode](../README.md#docusignAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web Form Instance with metadata |  -  |
**401** | The authentication information is either missing or invalid |  -  |
**403** | The requestor is not authorized |  -  |
**404** | The requested resource is not found |  -  |
**500** | The service encountered an unexpected condition that prevented it from fulfilling the request |  -  |
**503** | service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instances**
> WebFormInstanceList list_instances(account_id, form_id, client_user_id=client_user_id)

List instances

List all the instances of a web form in an account. When filtered by clientUserId, it will return instances having same clientUserId

### Example

* OAuth Authentication (docusignAccessCode):

```python
import openapi_client
from openapi_client.models.web_form_instance_list import WebFormInstanceList
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
    api_instance = openapi_client.FormInstanceManagementApi(api_client)
    account_id = 'account_id_example' # str | Account identifier in which the web form resides
    form_id = 'form_id_example' # str | Unique identifier for a web form that is consistent for it's lifetime
    client_user_id = 'client_user_id_example' # str | A unique identifier for a user that should originate from client's system. This value can be anything your backend system would use to track individual form instances. Examples include employee IDs, email addresses, surrogate key values, etc. (optional)

    try:
        # List instances
        api_response = api_instance.list_instances(account_id, form_id, client_user_id=client_user_id)
        print("The response of FormInstanceManagementApi->list_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormInstanceManagementApi->list_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account identifier in which the web form resides | 
 **form_id** | **str**| Unique identifier for a web form that is consistent for it&#39;s lifetime | 
 **client_user_id** | **str**| A unique identifier for a user that should originate from client&#39;s system. This value can be anything your backend system would use to track individual form instances. Examples include employee IDs, email addresses, surrogate key values, etc. | [optional] 

### Return type

[**WebFormInstanceList**](WebFormInstanceList.md)

### Authorization

[docusignAccessCode](../README.md#docusignAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all Web Form Instances with associated metadata. |  -  |
**401** | The authentication information is either missing or invalid |  -  |
**403** | The requestor is not authorized |  -  |
**404** | The requested resource is not found |  -  |
**500** | The service encountered an unexpected condition that prevented it from fulfilling the request |  -  |
**503** | Service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> WebFormInstance refresh_token(account_id, form_id, instance_id)

Refreshes the instance token

Generates new instance token for the existing Web Form Instance.

### Example

* OAuth Authentication (docusignAccessCode):

```python
import openapi_client
from openapi_client.models.web_form_instance import WebFormInstance
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
    api_instance = openapi_client.FormInstanceManagementApi(api_client)
    account_id = 'account_id_example' # str | Account identifier in which the web form resides
    form_id = 'form_id_example' # str | Unique identifier for a web form entity that is consistent for it's lifetime
    instance_id = 'instance_id_example' # str | Unique identifier for a Web Form Instance that is consistent until its expiration

    try:
        # Refreshes the instance token
        api_response = api_instance.refresh_token(account_id, form_id, instance_id)
        print("The response of FormInstanceManagementApi->refresh_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormInstanceManagementApi->refresh_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account identifier in which the web form resides | 
 **form_id** | **str**| Unique identifier for a web form entity that is consistent for it&#39;s lifetime | 
 **instance_id** | **str**| Unique identifier for a Web Form Instance that is consistent until its expiration | 

### Return type

[**WebFormInstance**](WebFormInstance.md)

### Authorization

[docusignAccessCode](../README.md#docusignAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web Form Instance with new instance token and metadata |  -  |
**400** | The instance token cannot be created, possibly because the validation failed. |  -  |
**401** | The authentication information is either missing or invalid |  -  |
**403** | The requestor is not authorized |  -  |
**404** | The requested resource is not found |  -  |
**500** | The service encountered an unexpected condition that prevented it from fulfilling the request |  -  |
**503** | service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

