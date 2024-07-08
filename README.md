# openapi-client
The Web Forms API facilitates generating semantic HTML forms around everyday contracts.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.1.0
- Package version: 1.0.0
- Generator version: 7.5.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://developers.docusign.com/](https://developers.docusign.com/)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
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
    except ApiException as e:
        print("Exception when calling FormInstanceManagementApi->create_instance: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://apps.docusign.com/api/webforms/v1.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FormInstanceManagementApi* | [**create_instance**](docs/FormInstanceManagementApi.md#create_instance) | **POST** /accounts/{accountId}/forms/{formId}/instances | Creates an instance of the web form
*FormInstanceManagementApi* | [**get_instance**](docs/FormInstanceManagementApi.md#get_instance) | **GET** /accounts/{accountId}/forms/{formId}/instances/{instanceId} | Get form instance
*FormInstanceManagementApi* | [**list_instances**](docs/FormInstanceManagementApi.md#list_instances) | **GET** /accounts/{accountId}/forms/{formId}/instances | List instances
*FormInstanceManagementApi* | [**refresh_token**](docs/FormInstanceManagementApi.md#refresh_token) | **POST** /accounts/{accountId}/forms/{formId}/instances/{instanceId}/refresh | Refreshes the instance token
*FormManagementApi* | [**get_form**](docs/FormManagementApi.md#get_form) | **GET** /accounts/{accountId}/forms/{formId} | Get Form
*FormManagementApi* | [**list_forms**](docs/FormManagementApi.md#list_forms) | **GET** /accounts/{accountId}/forms | List Forms


## Documentation For Models

 - [AuthenticationMethod](docs/AuthenticationMethod.md)
 - [CreateInstanceRequestBody](docs/CreateInstanceRequestBody.md)
 - [HttpError](docs/HttpError.md)
 - [HttpSuccess](docs/HttpSuccess.md)
 - [InstanceSource](docs/InstanceSource.md)
 - [InstanceStatus](docs/InstanceStatus.md)
 - [TemplateProperties](docs/TemplateProperties.md)
 - [WebForm](docs/WebForm.md)
 - [WebFormComponentType](docs/WebFormComponentType.md)
 - [WebFormContent](docs/WebFormContent.md)
 - [WebFormInstance](docs/WebFormInstance.md)
 - [WebFormInstanceEnvelopesInner](docs/WebFormInstanceEnvelopesInner.md)
 - [WebFormInstanceList](docs/WebFormInstanceList.md)
 - [WebFormInstanceMetadata](docs/WebFormInstanceMetadata.md)
 - [WebFormMetadata](docs/WebFormMetadata.md)
 - [WebFormProperties](docs/WebFormProperties.md)
 - [WebFormSource](docs/WebFormSource.md)
 - [WebFormState](docs/WebFormState.md)
 - [WebFormSummary](docs/WebFormSummary.md)
 - [WebFormSummaryList](docs/WebFormSummaryList.md)
 - [WebFormUserInfo](docs/WebFormUserInfo.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="docusignAccessCode"></a>
### docusignAccessCode

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://account.docusign.com/oauth/auth
- **Scopes**: N/A


## Author

devcenter@docusign.com


