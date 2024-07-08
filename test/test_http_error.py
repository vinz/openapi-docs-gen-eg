# coding: utf-8

"""
    Web Forms API version 1.1

    The Web Forms API facilitates generating semantic HTML forms around everyday contracts. 

    The version of the OpenAPI document: 1.1.0
    Contact: devcenter@docusign.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.http_error import HttpError

class TestHttpError(unittest.TestCase):
    """HttpError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HttpError:
        """Test HttpError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HttpError`
        """
        model = HttpError()
        if include_optional:
            return HttpError(
                error_code = '',
                message = ''
            )
        else:
            return HttpError(
        )
        """

    def testHttpError(self):
        """Test HttpError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
